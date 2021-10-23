import random

global polarizer, x_base, z_base, bit_length
polarizer = ["Ｘ", "＋"]
x_base = ["／", "＼"]
z_base = ["－", "｜"]
bit_length = 20

def get_measure_result(ones_polarizer, encoded_message):
    unpacked_message = []
    for i in range(bit_length):
        if(polarizer.index(ones_polarizer[i]) == 0):
            if(x_base.count(encoded_message[i]) == 0):
                unpacked_message.append(random.choice(x_base))
            else:
                unpacked_message.append(encoded_message[i])
        else:
            if(z_base.count(encoded_message[i]) == 0):
                unpacked_message.append(random.choice(z_base))
            else:
                unpacked_message.append(encoded_message[i])
    return unpacked_message

def compare_key(alice_key, bob_key):
    result = True
    for i in range(len(alice_key)):
        if(alice_key[i] != bob_key[i]):
            result = False
            break;
    return result

alice_bit = [random.randint(0, 1) for i in range(bit_length)]
print("Alice Bit:\t", *alice_bit)
alice_polarizer = [random.choice(polarizer) for i in range(bit_length)]
print("Alice Polarizer:", *alice_polarizer)
encoded_message = []
count = 0
for e in alice_polarizer:
    if(polarizer.index(e) == 0):
        encoded_message.append(x_base[alice_bit[count]])
        count += 1
    else:
        encoded_message.append(z_base[alice_bit[count]])
        count += 1
print("\nEncoded message:", *encoded_message)

eve_exist = random.choice([True, False])
if(eve_exist):
    print("\nEavesdropper exists.")
    eve_polarizer = [random.choice(polarizer) for i in range(bit_length)]
    print("Eve's Polarizer:    ", *eve_polarizer)
    encoded_message = get_measure_result(eve_polarizer, encoded_message)
    print("Manipulated Message:", *encoded_message)


bob_polarizer = [random.choice(polarizer) for i in range(bit_length)]
print("\nBob Polarizer:     ", *bob_polarizer)
bob_measure_result = get_measure_result(bob_polarizer, encoded_message)
print("Bob Measure Result:", *bob_measure_result)

print()

alice_key = []
for i in range(bit_length):
    if(alice_polarizer[i] == bob_polarizer[i]):
        alice_key.append(alice_bit[i])
print("Alice Key:", *alice_key)
bob_key = []
for i in range(bit_length):
    if(alice_polarizer[i] == bob_polarizer[i]):
        if(bob_polarizer[i] == "＋"):
            bob_key.append(z_base.index(bob_measure_result[i]))
        else:
            bob_key.append(x_base.index(bob_measure_result[i]))
print("Bob Key:  ", *bob_key, end='\n\n')
if(compare_key(alice_key, bob_key)):
    print("Key matched.")
else:
    print("Session failed, eavesdropper has interupted. Need to retry.")
