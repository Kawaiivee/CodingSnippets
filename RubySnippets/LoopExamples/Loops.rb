intArray = [3,1,4,1,5,9,6,2,8]
charArray = ['H','E','L','L','O']
strArray = ["I","love","you"]

#explicit (key is not of a data type) objKEY strDATA
hash1 = {"Ramir" => "Aguilos", "Kawaii" => "Vee", "Psycho" => "Tech87"}

#implicit (key MUST be a data type) charKEY intDATA
hash2 = {"k1" => 1, "k2" => 2, "k3" => 3, "k4" => 4}


#Iterative Loops For Data
for arg in intArray
    puts arg
end

for arg in charArray
    puts arg
end

for arg in strArray
    puts arg
end

i = 0
while i < intArray.size
    puts intArray[i]
    i += 1
end

print "Items in hash1:"
puts hash1.size

hash1.each_key do |key, val|
    puts key + ":" + hash1[key]
end

print "Items in hash2: "
puts hash2.size

hash2.each_key do |key, val|
    puts key + ": %f " % hash2[key] + hash2[key].to_s
end

for i in 0..5
    if intArray[i] < 2
        next
    end
    puts intArray[i]
end

j = 0
while j < 5
    if charArray[j] == 'L'
        puts "Removed L's"
        j += 1
        next
    end
    puts charArray[j]
    j += 1
end
