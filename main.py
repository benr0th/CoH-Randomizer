import random
import replit
from bullet import Bullet
from getkey import getkey, keys

replit.clear()

archetypes = ["Blaster", "Controller", "Defender", "Scrapper", "Tanker", "Brute", "Stalker", "Mastermind", "Dominator", "Corruptor"]

hc = list(archetypes)
hc.insert(5, "Sentinel")
rb = list(archetypes)
rb.insert(5, "Guardian")
tspy = list(archetypes)
tspy.insert(5, "Primalist")
nd = list(archetypes)
nd[5:5] = ["Sentinel", "Paragon", "Templar War Child", "Transmorpher", "Kheldian Royal Guard", "Blapper", "Patron Master", "Shield Expert", "Freakshow", "Signature Series", "Warriors of Avalon", "Evolutionary Leap", "Synergist", "Primalist", "Kill Team"]

origins = ["Science", "Mutation", "Magic", "Technology", "Natural"]

alignment = ["Hero", "Villain"]

bodyType = ["Male", "Female", "Huge"]

blaster = [[]]

blasterHC = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"],
["Atomic Manipulation", "Devices", "Darkness Manipulation", "Earth Manipulation", "Energy Manipulation", "Electricity Manipulation", "Fire Manipulation", "Ice Manipulation", "Martial Combat", "Mental Manipulation", "Ninja Training", "Plant Manipulation", "Sonic Manipulation", "Tactical Arrow", "Temporal Manipulation"]]

blasterRB = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Sonic Attack", "Water Blast"],
["Devices", "Darkness Manipulation", "Energy Manipulation", "Electricity Manipulation", "Fire Manipulation", "Ice Manipulation", "Martial Combat", "Mental Manipulation"]]

blasterTSPY = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Sonic Attack", "Water Blast"],
["Devices", "Darkness Manipulation", "Energy Manipulation", "Electricity Manipulation", "Fire Manipulation", "Ice Manipulation", "Martial Combat", "Mental Manipulation", "Radiation Manipulation", "Temporal Manipulation"]]

controller = [[]]

controllerHC = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control"],
["Cold Domination", "Darkness Affinity", "Electrical Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"]]

controllerRB = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control", "Water Control", "Wind Control"],
["Cold Domination", "Darkness Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Trick Arrow"]]

controllerTSPY = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control", "Water Control", "Wind Control"],
["Cold Domination", "Darkness Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Trick Arrow", "Traps"]]

defender = [[]]

defenderHC = [["Cold Domination", "Dark Miasma", "Electrical Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"],
["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"]]

defenderRB = [["Cold Domination", "Dark Miasma", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"],
["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Sonic Attack", "Water Blast"]]

defenderTSPY = [["Cold Domination", "Dark Miasma", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"],
["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fiery Combat", "Icy Combat", "Psychic Blast", "Holy Light", "Radiation Blast", "Sonic Attack", "Water Blast", "Earth Combat", "Kinetic Assault", "Martial Combat", "Thorny Combat", "Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Katana", "Savage Melee", "Street Justice", "War Mace", "Staff Fighting"]]

scrapper = [[]]

scrapperHC = [["Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Dark Melee", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Katana", "Kinetic Melee", "Martial Arts", "Psionic Melee", "Radiation Melee", "Savage Melee", "Stone Melee", "Spines", "Staff Fighting", "Street Justice", "Titan Weapons", "War Mace"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Shield Defense", "Stone Armor", "Super Reflexes", "Willpower"]]

scrapperRB = [["Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Dark Melee", "Electrical Melee", "Fiery Melee", "Ice Melee", "Katana", "Kinetic Melee", "Martial Arts", "Psionic Melee", "Radiation Melee", "Savage Melee", "Spines", "Staff Fighting", "Street Justice", "Titan Weapons", "War Mace"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Shield Defense", "Super Reflexes", "Willpower"]]

tanker = [[]]

tankerOG = [["Bio Armor", "Dark Armor", "Electric Armor", "Fiery Aura", "Ice Armor", "Invulnerability", "Radiation Armor", "Shield Defense", "Stone Armor", "Super Reflexes", "Willpower"],
["Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Dark Melee", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Katana", "Kinetic Melee", "Martial Arts", "Psionic Melee", "Radiation Melee", "Savage Melee", "Stone Melee", "Spines", "Staff Fighting", "Street Justice", "Super Strength", "Titan Weapons", "War Mace"]]

tankerTSPY = [["Bio Armor", "Dark Armor", "Electric Armor", "Fiery Aura", "Ice Armor", "Invulnerability", "Radiation Armor", "Shield Defense", "Stone Armor", "Super Reflexes", "Willpower", "Sacred Armor"],
["Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Dark Melee", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Katana", "Kinetic Melee", "Martial Arts", "Psionic Melee", "Radiation Melee", "Savage Melee", "Stone Melee", "Spines", "Staff Fighting", "Street Justice", "Super Strength", "Titan Weapons", "War Mace", "Hard Life", "Pale Blade"]]

sentinel = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Super Reflexes", "Willpower"]]

brute = [["Battle Axe", "Broad Sword", "Claws", "Dual Blades", "Dark Melee", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Katana", "Kinetic Melee", "Martial Arts", "Psionic Melee", "Radiation Melee", "Savage Melee", "Stone Melee", "Spines", "Staff Fighting", "Street Justice", "Super Strength", "Titan Weapons", "War Mace"],
["Bio Armor", "Dark Armor", "Electric Armor", "Fiery Aura", "Ice Armor", "Invulnerability", "Radiation Armor", "Regeneration", "Shield Defense", "Stone Armor", "Super Reflexes", "Willpower"]]

stalker = [[]]

stalkerHC = [["Broad Sword", "Claws", "Dark Melee", "Dual Blades", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Kinetic Melee", "Martial Arts", "Ninja Blade", "Psionic Melee", "Radiation Melee", "Savage Melee", "Spines", "Staff Fighting", "Stone Melee", "Street Justice"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Shield Defense", "Stone Armor", "Super Reflexes", "Willpower"]]

stalkerRB = [["Broad Sword", "Claws", "Dark Melee", "Dual Blades", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Kinetic Melee", "Martial Arts", "Ninja Blade", "Psionic Melee", "Radiation Melee", "Savage Melee", "Spines", "Staff Fighting", "Street Justice"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Super Reflexes", "Willpower"]]

stalkerTSPY = [["Broad Sword", "Claws", "Dark Melee", "Dual Blades", "Electrical Melee", "Energy Melee", "Fiery Melee", "Ice Melee", "Kinetic Melee", "Martial Arts", "Ninja Blade", "Psionic Melee", "Radiation Melee", "Savage Melee", "Spines", "Staff Fighting", "Street Justice", "Spectral Melee"],
["Bio Armor", "Dark Armor", "Electric Armor", "Energy Aura", "Fiery Aura", "Ice Armor", "Invulnerability", "Ninjitsu", "Radiation Armor", "Regeneration", "Super Reflexes", "Willpower", "Spectral Aura"]]

mastermind = [[]]

mastermindHC = [["Beast Mastery", "Demon Summoning", "Mercenaries", "Necromancy", "Ninjas", "Robotics", "Thugs"],
["Cold Domination", "Dark Miasma", "Electrical Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"]]

mastermindRB = [["Beast Mastery", "Demon Summoning", "Mercenaries", "Necromancy", "Ninjas", "Robotics", "Thugs"],
["Cold Domination", "Dark Miasma", "Force Field", "Nature Affinity", "Pain Domination", "Poison", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"]]

mastermindTSPY = [["Beast Mastery", "Demon Summoning", "Mercenaries", "Necromancy", "Ninjas", "Robotics", "Thugs", "Knights"],
["Cold Domination", "Dark Miasma", "Force Field", "Nature Affinity", "Pain Domination", "Poison", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow", "Obedience Training"]]

dominator = [[]]

dominatorHC = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control"],
["Dark Assault", "Earth Assault", "Electricity Assault", "Energy Assault", "Fiery Assault", "Icy Assault", "Martial Assault", "Psionic Assault", "Radioactive Assult", "Savage Assault", "Thorny Assault"]]

dominatorRB = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control", "Water Control", "Wind Control"],
["Dark Assault", "Earth Assault", "Electricity Assault", "Energy Assault", "Fiery Assault", "Icy Assault", "Kinetic Assault", "Martial Assault", "Psionic Assault", "Thorny Assault"]]

dominatorTSPY = [["Darkness Control", "Earth Control", "Electric Control", "Fire Control", "Gravity Control", "Ice Control", "Illusion Control", "Mind Control", "Plant Control", "Water Control", "Wind Control"],
["Atomic Assault", "Dark Assault", "Earth Assault", "Electricity Assault", "Energy Assault", "Fiery Assault", "Icy Assault", "Kinetic Assault", "Martial Assault", "Psionic Assault", "Psychokinetic Assault", "Thorny Assault"]]

corruptor = [[]]

corruptorHC = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"],
["Cold Domination", "Dark Miasma", "Electrical Affinity", "Empathy", "Force Field", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"]]

corruptorRB = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"],
["Cold Domination", "Dark Miasma", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow"]]

corruptorTSPY = [["Archery", "Assault Rifle", "Beam Rifle", "Dark Blast", "Dual Pistols", "Electrical Blast", "Energy Blast", "Fire Blast", "Ice Blast", "Psychic Blast", "Radiation Blast", "Seismic Blast", "Sonic Attack", "Water Blast"],
["Cold Domination", "Dark Miasma", "Kinetics", "Nature Affinity", "Pain Domination", "Poison", "Radiation Emission", "Sonic Resonance", "Storm Summoning", "Thermal Radiation", "Time Manipulation", "Traps", "Trick Arrow", "Force Field"]]

guardian = [["Dark Assault", "Earth Assault", "Electricity Assault", "Energy Assault", "Fiery Assault", "Gun Fu", "Hellfire Assault", "Icy Assault", "Kinetic Assault", "Luminous Assault", "Mace Assault", "Martial Assault", "Military Assault", "Ninja Assault", "Psionic Assault", "Radiation Assault", "Thorny Assault", "Umbral Assault"],
["Atmospheric Composition", "Dark Composition", "Energy Composition", "Fiery Composition", "Ice Composition", "Infiltrator Training", "Organic Composition", "Pain Focusing", "Radiation Composition", "Reconstructive Healing", "Stone Composition", "Temporal Reaction"]]

def rando(arch):
    print(arch)
    
    if arch == "Blaster":
        print(random.choice(blaster[0]))
        print(random.choice(blaster[1]))
    elif arch == "Controller":
        print(random.choice(controller[0]))
        print(random.choice(controller[1]))
    elif arch == "Defender":
        print(random.choice(defender[0]))
        print(random.choice(defender[1]))
    elif arch == "Scrapper":
        print(random.choice(scrapper[0]))
        print(random.choice(scrapper[1]))
    elif arch == "Tanker":
        print(random.choice(tanker[0]))
        print(random.choice(tanker[1]))
    elif arch == "Sentinel":
        print(random.choice(sentinel[0]))
        print(random.choice(sentinel[1]))
    elif arch == "Brute":
        print(random.choice(brute[0]))
        print(random.choice(brute[1]))
    elif arch == "Stalker":
        print(random.choice(stalker[0]))
        print(random.choice(stalker[1]))
    elif arch == "Mastermind":
        print(random.choice(mastermind[0]))
        print(random.choice(mastermind[1]))
    elif arch == "Dominator":
        print(random.choice(dominator[0]))
        print(random.choice(dominator[1]))
    elif arch == "Corruptor":
        print(random.choice(corruptor[0]))
        print(random.choice(corruptor[1]))
    elif arch == "Guardian":
        print(random.choice(guardian[0]))
        print(random.choice(guardian[1]))


def tutorial():
  print("Arrow keys to navigate, Press ENTER to select\n")

def mainMenu():
  replit.clear()
  
  server = Bullet(
    prompt = "Select your server: ",
    choices = ["Homecoming", "Rebirth", "Thunderspy"],
    bullet = ""
  )
  print("Arrow keys to navigate, Press ENTER to select\n")
  global serverArch
  serverArch = server.launch()
  
  replit.clear()

def randoMenu():
  print("")
  randoMenu = Bullet(
    choices = ["Randomize all", "Choose archetype", "Choose another server"],
    bullet = ""
  )
  global randoSelect
  randoSelect = randoMenu.launch()
  replit.clear()

def archMenu():
  replit.clear()
    
  archMenu = Bullet(
    choices = hc if serverArch == "Homecoming" else rb if       serverArch == "Rebirth" else tspy if serverArch == "Thunderspy" else "",
      bullet = ""
  )
  
  tutorial()
  global result
  result = archMenu.launch()
  replit.clear()
  tutorial()
  rando(result)

def endMenu():
  print("")
  endMenu = Bullet(
    choices = ["Randomize again", "Choose another archetype", "Randomize all", "Choose another server"],
    bullet = "",
    return_index = True
  )
  global endMenuSelect
  endMenuSelect = endMenu.launch()

def serverChoice():
  global randoArch
  global blaster
  global controller
  global defender
  global scrapper
  global tanker
  global stalker
  global mastermind
  global dominator
  global corruptor
  if serverArch == "Homecoming":
    blaster = blasterHC
    controller = controllerHC
    defender = defenderHC
    scrapper = scrapperHC
    tanker = tankerOG
    stalker = stalkerHC
    mastermind = mastermindHC
    dominator = dominatorHC
    corruptor = corruptorHC
    randoArch = random.choice(hc)
  elif serverArch == "Rebirth":
    blaster = blasterRB
    controller = controllerRB
    defender = defenderRB
    scrapper = scrapperRB
    tanker = tankerOG
    stalker = stalkerRB
    mastermind = mastermindRB
    dominator = dominatorRB
    corruptor = corruptorRB
    randoArch = random.choice(rb)
  elif serverArch == "Thunderspy":
    blaster = blasterTSPY
    controller = controllerTSPY
    defender = defenderTSPY
    scrapper = scrapperRB
    tanker = tankerTSPY
    stalker = stalkerTSPY
    mastermind = mastermindTSPY
    dominator = dominatorTSPY
    corruptor = corruptorTSPY
    randoArch = random.choice(tspy)

def start():
  mainMenu()
  serverChoice()
  tutorial()
  rando(randoArch)
  # print("")
  # print("Alignment: " + random.choice(alignment))
  # print("Origin: " + random.choice(origins))
  # print("Body Type: " + random.choice(bodyType))
  randoMenu()

start()

def phase1():
  global randoSelect
  while True:
    tutorial()
    if randoSelect == "Randomize all":
      serverChoice()
      rando(randoArch)
      # print("")
      # print("Alignment: " + random.choice(alignment))
      # print("Origin: " + random.choice(origins))
      # print("Body Type: " + random.choice(bodyType))
      randoMenu()
    elif randoSelect == "Choose archetype":
      randoSelect = ""
      archMenu()
      endMenu()
      phase2()
    elif randoSelect == "Choose another server":
      start()

def phase2():
  global randoSelect
  while True:
    if endMenuSelect[1] == 0:
      replit.clear()
      tutorial()
      rando(result)
      endMenu()
    elif endMenuSelect[1] == 1:
      randoSelect = "Choose archetype"
      phase1()
    elif endMenuSelect[1] == 2:
      randoSelect = "Randomize all"
      replit.clear()
      phase1()
    elif endMenuSelect[1] == 3:
      randoSelect = "Choose another server"
      phase1()

phase1()
