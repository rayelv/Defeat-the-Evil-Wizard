# Base Character class
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        '''Updating the attack function to deal amount of damage randomly'''
        self.attack_power = random.randint(15,30)
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    #Adding healing mechanic
    def heal(self):
        heal_amount = random.randint(10,20)
        '''Implementing randomisation to give healing points'''
        new_health = self.health + heal_amount
        if new_health > self.max_health:
            '''Health set to max health to avoid going over'''
            self.health = self.max_health
            print(f'{self.name} has healed up to {heal_amount} points, maximum health reached.' )
        else:
            print(f'{self.name} heals for {heal_amount}. Current health: {new_health}')
            
    #Adding option to use special abilities        
    def use_special_ability(self,opponent):
        '''Default if character has no abiliies'''
        print(f'{self.name} has no special abilities.')
                
        
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health= 140, attack_power=25)
        
    def flame_tiger(self,opponent):
        damage = random.randint(50,100)
        opponent.health -= damage
        if opponent.health <= 0:
            print(f'{self.name} attacks with 🔥Flaming Tiger🔥. Opponent is done and toasted! {self.name} WINS.')
        else:
            print(f'{self.name} attacks with 🔥Flaming Tiger🔥. Damage dealt: {damage}.')
            
    def crest_protection(self):
        #self.health = self.health
        print(f'{self.name} is using 🪬Crest Protection🪬 to avoid the oncoming damage.')
        
    '''Overriding the parent method for specific character '''
    def use_special_ability(self, opponent):
        choice = input('-----.✨Abilities✨-----\n1.🔥Flame Tiger🔥\n2.🪬Crest Protection🪬\n Choose your ability:\n')
        if choice == '1':
            self.flame_tiger(opponent)
        elif choice == '2':
            self.crest_protection()
        else:
            print('Invalid choice.')
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health= 100, attack_power=35)
        
    def exploding_blood(self,opponent):
        damage = random.randint(35,60)
        opponent.health -= damage
        if opponent.health <= 0:
            print(f'{self.name} has taken out the Wizard!')
        
    def thunder_clap(self,opponent):
        '''Drastic damage, half of opponent health taken away '''
        damage = opponent.health / 2
        opponent.health -= damage
        if opponent.health <= 0:
            print(f'{self.name} has taken out the Wizard with ⚡Thunder Clap⚡!')
        else:
            print(f'{self.name} attacks using ⚡Thunder Clap⚡.')
        
    def use_special_ability(self, opponent):
        choice = input('-----.✨Abilities✨-----\n1.🩸🧨Exploding Blood🩸🧨\n2.⚡Thunder Clap⚡\n Choose your ability:\n')
        if choice == '1':
            self.exploding_blood(opponent)
        elif choice == '2':
            self.thunder_clap(opponent)
        else:
            print('Invalid choice.')
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health= 150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
# Create Archer class
class Archer(Character):
    def __init__(self,name):
        super().__init__(name, health=130, attack_power=35)
        
    def quick_shot(self,opponent):
        '''Double attack'''
        damage = self.attack_power * 2
        opponent.health -= damage
        if opponent.health <= 0:
            return(f'{self.name} used 🏹Quick Shot🏹 to deal {damage} damage! Opponent has been defeated!')
        else:
            print(f'{self.name} used 🏹Quick Shot🏹 to deal {damage} damage!')
      
    def evade(self):
        print(f'{self.name} has evaded the attack! 🏃‍♂️‍➡️ Current health: {self.health}')     
        
    def use_special_ability(self, opponent):
        choice = input('-----.✨Abilities✨-----\n1.🏹Quick Shot🏹\n2.🏃‍♂️‍➡️Evade🏃‍♂️‍➡️\n Choose your ability:\n')
        if choice == '1':
            self.quick_shot(opponent)
        elif choice == '2':
            self.evade()
        else:
            print('Invalid choice.')
# Create Paladin class 
class Paladin(Character):
    def __init__(self,name):
        super().__init__(name, health=150, attack_power=30)
        
    def holy_strike(self,opponent):
        '''Bonus damage'''
        damage = random.randint(35,40) + random.randint(10,30)
        opponent.health -= damage
        if opponent.health <= 0:
            return (f'{self.name} has released 💥HOLY STRIKE💥 Damage dealt : {damage}. Opponent has been defeated!')
        else:
            print(f'{self.name} has released 💥HOLY STRIKE💥 Damage dealt : {damage}')
        
    def divine_shield(self):
        print(f'{self.name} activates 🛡️Divine Shield🛡️ to block the next attack! Current health: {self.health}')
        
    def use_special_ability(self, opponent):
        choice = input('-----.✨Abilities✨-----\n1.💥Holy Strike💥\n2.🛡️Divine Protection🛡️\n Choose your ability:\n')
        if choice == '1':
            self.holy_strike(opponent)
        elif choice == '2':
            self.divine_shield()
        else:
            print('Invalid choice.')
        
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: \n")
    name = input("Enter your character's name: \n").capitalize()

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action:\n")

        if choice == '1':
            player.attack(wizard)
            '''Polymorphism will show selected characters ability'''
        elif choice == '2':
            player.use_special_ability(wizard)   
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
