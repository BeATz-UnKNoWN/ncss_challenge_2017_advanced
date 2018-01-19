from tamagotchi import Tamagotchi

commands = ["create", "feed", "play", "wait"]
tamagotchis = {}
for command in iter(input("Command: "), ""):
  cmd = command.split()
  roundInvalid = False
  if cmd[0] in commands:
    if cmd[0] == commands[0]:
      if cmd[1] in tamagotchis:
        if tamagotchis[cmd[1]].is_dead():
          tamagotchis.pop(cmd[1])
          new = Tamagotchi(cmd[1])
          tamagotchis[cmd[1]] = new
        else: print("You already have a Tamagotchi called that.");roundInvalid=True
      else:
        new = Tamagotchi(cmd[1])
        tamagotchis[cmd[1]] = new
    elif cmd[0] == commands[1]:
      if cmd[1] not in tamagotchis:
        print("No Tamagotchi with that name.")
        roundInvalid=True
      else: tamagotchis[cmd[1]].feed()
    elif cmd[0] == commands[2]:
      if cmd[1] not in tamagotchis:
        print("No Tamagotchi with that name.")
        roundInvalid=True
      else: tamagotchis[cmd[1]].play()
    #elif cmd[0] == commands[3]: #do nothing
    if not roundInvalid:
      for tam in sorted(tamagotchis): print(str(tamagotchis[tam]))
      for tam in tamagotchis: tamagotchis[tam].increment_time()
  else: print("Invalid command.")