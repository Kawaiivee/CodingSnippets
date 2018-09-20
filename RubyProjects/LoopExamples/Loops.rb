intArray = [3,1,4,1,5,9]
charArray = ['H','E','L','L','O']
strArray = ["I","love","you"]

#explicit (key is not of a data type) objKEY strDATA
hash1 = {"Ramir" => "Aguilos", "Kawaii" => "Vee", "Psycho" => "Tech87"}

#implicit (key MUST be a data type) charKEY intDATA
hash2 = {"k1" => 1, "k2" => 2, "k3" => 3, "k4" => 4}


#Iterative Loops For data
for arg in intArray
    puts arg
end

for arg in charArray
    puts arg
end

for arg in intArray
    puts arg
end

for arg in strArray
    puts arg
end

puts hash1.size

hash1.each_key do |key, val|
    puts key
    puts hash1[key]
end

hash2.each_key do |key, val|
    puts key
    puts hash2[key]
end
