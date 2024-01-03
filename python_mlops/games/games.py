import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class Player:
    def __init__(self):
        self.level = 1
        self.skill_points = 0
        self.hp = 100
        self.skills = {
            "Programming": 0,
            "Data Analysis": 0,
            "Machine Learning": 0,
            "Data Visualization": 0,
        }

    def level_up(self):
        self.skill_points += 1
        messagebox.showinfo("Level Up!", f"Congratulations! You've leveled up to Level {self.level}!\nYou've earned 1 skill point. Total skill points: {self.skill_points}")
        self.display_status()

    def display_status(self):
        status_info = f"Level: {self.level}\nHP: {self.hp}\nSkill Points: {self.skill_points}\n"
        for skill, level in self.skills.items():
            status_info += f"{skill}: Level {level}\n"
        messagebox.showinfo("Player Status", status_info)

    def increase_skill(self, skill):
        self.skills[skill] += 1
        messagebox.showinfo("Skill Increase", f"Your {skill} skill has increased to Level {self.skills[skill]}!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            messagebox.showinfo("Defeat", "You were defeated. Game Over!")
            return False
        else:
            self.display_status()
            return True

class Monster:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = 20 * difficulty

    def attack(self):
        damage = random.randint(1, self.difficulty) * 5
        messagebox.showinfo("Monster Attack!", f"{self.name} attacks! You take {damage} damage.")
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            messagebox.showinfo("Victory!", f"You defeated the {self.name} and gained experience!")
            return False
        else:
            messagebox.showinfo("Monster Hit!", f"{self.name} takes {damage} damage. {self.name}'s HP: {self.hp}")
            return True

class AdventureGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Science Adventure Game")

        self.player = Player()
        self.monsters = [Monster("Data Gremlin", 1), Monster("Algorithm Ogre", 2), Monster("Visualization Vampire", 3)]
        self.current_monster = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to the Data Science Adventure Game!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.battle_button = tk.Button(self.master, text="Battle a Monster", command=self.battle_monster)
        self.battle_button.pack(pady=5)

        self.check_skills_button = tk.Button(self.master, text="Check Skills", command=self.player.display_status)
        self.check_skills_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack(pady=5)

    def battle_monster(self):
        if not self.current_monster or self.current_monster.hp <= 0:
            self.current_monster = random.choice(self.monsters)
            messagebox.showinfo("Monster Encounter", f"You encounter a {self.current_monster.name} (Difficulty: {self.current_monster.difficulty})!")

        player_damage = random.randint(1, self.player.skills["Machine Learning"] + 1) * 20
        monster_damage = self.current_monster.attack()

        player_alive = self.player.take_damage(monster_damage)
        monster_alive = self.current_monster.take_damage(player_damage)

        if not player_alive or not monster_alive:
            self.end_battle()

        if player_alive and self.player.skill_points > 0:
            self.prompt_skill_increase()

    def prompt_skill_increase(self):
        response = messagebox.askquestion("Skill Increase", "Would you like to increase a skill?")
        if response == 'yes':
            skill_to_increase = simpledialog.askstring("Skill Selection", "Which skill would you like to increase?")
            if skill_to_increase in self.player.skills:
                self.player.increase_skill(skill_to_increase)
                self.player.skill_points -= 1
                messagebox.showinfo("Skill Increase", f"You've increased your {skill_to_increase} skill!")
                self.player.display_status()

    def end_battle(self):
        self.current_monster = None
        if self.player.hp > 0:
            self.player.level_up()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGameApp(root)
    root.mainloop()
