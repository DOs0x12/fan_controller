def switch_fan(current_state: bool)->bool:
    print('info: the fan is switched to ', end='')
    state = not current_state
    print(state)
    
    return state