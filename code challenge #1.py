def sorting(str):
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
    index_list = []
    character_list = list(order)
    final_word = ""
    for character in str:
        pos = order.index(character)
        index_list.append(pos)
        character_list[pos] = character
    for num in sorted(index_list):
        final_word += character_list[num]
    return final_word
        
