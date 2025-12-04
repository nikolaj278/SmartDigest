from src.config.settings import COMMAND_EN, COMMAND_RU

def build_the_prompt(msgs):
    """ Build a prompt of the command and texts and authors of messges. """
    
    langs = [1 if m.language == "ru" else 0 for m in msgs]
    
    if sum(langs)/len(langs) >= 0.5: 
        command = COMMAND_RU
    else:
        command = COMMAND_EN
        
    return command + "\n".join([m.author_name + ":\n" + m.text for m in msgs])
