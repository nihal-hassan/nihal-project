from memory import DebateState
from qwen_utils import generate_response

def judge_agent(state: DebateState):
    """
    Evaluates the full debate history and declares a winner.
    Expects the LLM to respond starting with 'Winner: Pro' or 'Winner: Con'.
    """
    topic = state["topic"]
    history = "\n".join(state["history"])
    
    system_prompt = (
        "You are a professional Debate Judge. You must evaluate the conversation history. "
        "Decide who won (Pro or Con) and provide a concise reason. "
        "Your response MUST start with 'Winner: Pro' or 'Winner: Con'."
    )
    
    user_prompt = f"Topic: '{topic}'\nDebate history:\n{history}\n\nFinal verdict:"
    
    response = generate_response(system_prompt, user_prompt)
    
    # Clean up formatting like **** or extra spaces
    clean_response = response.replace("*", "").strip()
    
    winner = "Unknown"
    reason = clean_response
    
    if "Winner: Pro" in clean_response:
        winner = "Pro"
        reason = clean_response.split("Winner: Pro")[-1].strip()
    elif "Winner: Con" in clean_response:
        winner = "Con"
        reason = clean_response.split("Winner: Con")[-1].strip()
        
    # Remove leading colons or dashes if the model added them
    reason = reason.lstrip(": - \n")
            
    return {"winner": winner, "judge_reason": reason}
