#list methods

  #Indexing allows you to access individual values from a sequence. 
  #slicing:extract, modify and replace a specific range of elements from sequences.
  #Slicing allows you to extract a portion of a list.
  #Starting and stopping indexes are separated by a colon ":"
  #The starting index is inclusive. The stopping index is exclusive.
  #omit the starting index means that you'll be slicing from the very first element.  
  #[:n] means slicing from "0" index to "n".
  #[n:] means slicing from "n" index to "last".
  #[:] means slicing from "0" index to "last".
  #Python supports "indexing from the end", called negative indexing.EX=>-4"BD"-3"PAK"-2"NZ"-1"AUS"
  #always use less negative index then : then upper negative index.EX=>[-4:-2]. 

Country = ["BD","PAK","NZ","AUS"] #for slicing applied:0"BD"1"PAK"2"NZ"3"AUS"4   

pak = Country[1]

print(Country[0:2])#'BD','PAK'
print(Country[2:4])#'NZ','AUS'
print(Country[1:-2])#'PAK'
print(pak[1:3])#AK
print(pak[:2])#PA
print(Country[:3]) #'BD','PAK','NZ' .omit the starting index. 

Country[:3] = ["Wales","USA","UK"]#Updating country using slicing
print(Country) #['Wales', 'USA', 'UK', 'AUS']
