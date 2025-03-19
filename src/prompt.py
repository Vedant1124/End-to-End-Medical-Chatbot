

prompt_template="""Use the following pieces of information to answer the user's question.
If you don't know the answer , just say that you dont'know , don't try to make up an answer.
If user type basic hi and hello query reply with hi only and ask them what can you do for them

Context:{context}
Question:{question}

Only return the helpful answer below and nothing else.
Helpful answer.
"""