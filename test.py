import secrets

def main():
  target_str = input("input your string here: ")
  target_str_array =  target_str.split(" ")
  result_array_final = [[0] for n in target_str_array]
  for index_all, word in enumerate(target_str_array):
     print(index_all)
     result_array = [0 for n in word + word]
     for index in range(0,len(word)):
      if word[index].isalpha():
        first_num = secrets.randbelow(63) + 10
        second_num = first_num + ord(word[index]) - ord('a') + 1
        first_num_index = index
        second_num_index = len(word) + index
        result_array[first_num_index] = first_num
        result_array[second_num_index] = second_num
        print(f'first number is: {first_num}, second number is: {second_num}\nplaced in: {first_num_index}, and: {second_num_index}')
      print(f'resulting in {result_array}')
     result_array_final[index_all] =  result_array
  return result_array_final



def decoder(encoded_array):
  for char_bytes in encoded_array:
    decoded_string = [0 for n in range(0, len(char_bytes)//2)]
    for index in range(0, len(char_bytes)//2):
      decoded_string[index] = chr(char_bytes[index + len(char_bytes)//2] - char_bytes[index] + ord('a') - 1)
    print(decoded_string)

def stringFinal(encoded_array):
  temp = [0 for n in encoded_array]
  for index,an_array in enumerate(encoded_array):
    temp[index] = "".join([str(num) for num in an_array])
  print( " ".join(temp))
  return " ".join(temp)

def stringDecoder(some_string):
  temp_array = some_string.split(" ")
  temp_array_final = [[0] for n in temp_array]
  for index_all, char_array in enumerate(temp_array):
    temp_string = [0 for n in range(0, len(char_array)//2)]
    for index in range(0, len(char_array)//2):
      temp_string[index] = int(f'{char_array[index * 2]}{char_array[index * 2 + 1]}')
    temp_array_final[index_all] = temp_string
  decoder(temp_array_final)
  

encode = main()
decoder(encode)
stringFinal(encode)
stringDecoder("4116522414435747215736235764 24124148384572404332595357647744 431232583352 216023443819238141584323 641623793743")