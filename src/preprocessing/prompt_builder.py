def build_the_prompt(msgs, command):
    """ Build a prompt of the command and texts and authors of messges. """

    return command + "\n".join([m.author_name + ":\n" + m.text for m in msgs])
