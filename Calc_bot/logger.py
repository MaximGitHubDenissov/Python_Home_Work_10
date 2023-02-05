def log (text, res):
    with open('log.csv', 'a') as f:
        f.write(text)
        f.write(str(*res))
        
        