intArray = [3,1,4,1,5,9]
charArray = ['H','E','L','L','O']
strArray = ["I","love","you"]

#explicit (key is not of a data type) objKEY strDATA
hash1 = {"Ramir" => "Aguilos", "Kawaii" => "Vee", "Psycho" => "Tech87"}

#implicit (key MUST be a data type) charKEY intDATA
hash2 = {"k1" => 1, "k2" => 2, "k3" => 3, "k4" => 4}

for arg in intArray
    puts arg
end

x = 0
for x in charArray.length
    puts charArray[x]
    x += 1
end
