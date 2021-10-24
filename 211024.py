def solution(s):
    container = ['zero', 'one', 'two', 'three', 'four', 
               'five', 'six', 'seven', 'eight', 'nine']

    for number, string in enumerate(container):
        s = s.replace(string, str(number))
        
    return int(s)