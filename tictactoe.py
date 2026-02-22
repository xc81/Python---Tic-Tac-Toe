
in_game = True
play=True

class Player:
   def __init__(self, symbol, name):
      self.symbol = symbol
      self.name = name
      
   def pos(self):
      while True:
         try:
            choice =  input(f"Choix de {self.name} (symbole : {self.symbol}) sous format (x,y) : ").split(",")
            print("")
            try:
               x,y=map(int, choice)
            except:
               raise ValueError("coordonnées non-entières.")
            if not(1<=x<=3 and 1<=y<=3):
               raise ValueError("coordonnées incorrectes.")

            if grid[y-1][x-1] != "-" :
               raise ValueError("case déjà occupée.")

            grid[y-1][x-1] = self.symbol
            break
         except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

class Game:
   def _init__(self):
      pass

   def are_colinear(self, u, v):
      '''
      On vérifie que les vecteurs u et v sont colinéaires.
      '''
      return u[0]*v[1] - u[1]*v[0]==0

   def coord_list(self, symbol, grid):
      list_coord=[]
      for i in range(3):
         for j in range(3):
            if grid[i][j]==symbol:
               list_coord.append([j,i])
      return list_coord

   def check(self, player, grid, list_coord):
      '''
      On vérifie qu'il existe trois points alignés, et on procède en calculant la colinéarité
      de deux des vecteurs formés par les trois points.
      '''
      state=False
      for i in range(len(list_coord)):
         xi, yi=list_coord[i]
         for j in range(i+1, len(list_coord)):
            xj, yj=list_coord[j]
            for k in range(j+1, len(list_coord)):
               xk, yk=list_coord[k]
               if self.are_colinear((xj-xi,yj-yi), (xk-xj,yk-yj)):
                  state=True
                  return state
      return state

   def draw(self, grid):
      print("")
      for i in range(3):
         for j in range(3):
            print(grid[i][j], " ", end="")
         print("")
      print("")

while play:

   user_choice=input(("Bienvenue au jeu du Morpion. Entrez 'oui' pour débuter une nouvelle partie : "))
   if user_choice=="oui":
      grid=[
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
         ]

      game=Game()
      player1 = Player("X", input("Entrez le pseudo du premier joueur : "))
      player2 = Player("O", input("Entrez le pseudo du deuxième joueur : "))
            
      while in_game:
         
         game.draw(grid)

         player1.pos()
         list1=game.coord_list(player1.symbol, grid)
         if game.check(player1, grid, list1)==True:
            print(f"Victoire de {player1.name} !")
            print("")
            in_game=False

         player2.pos()
         list2=game.coord_list(player2.symbol, grid)
         if game.check(player2, grid, list2)==True:
            print(f"Victoire de {player2.name} !")
            print("")
            in_game=False
   else:
      print("Au revoir !")
      play=False
