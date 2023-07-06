# class Student:
#      school="Akirachix"
#      def __init__(self,name,age,nationality):
#         self.name=name
#         self.age=age
#         self.nationality=nationality
#      def greet_student(self):
#          return f"hello{self.name} welcome to {self.school}"
#      def  year_of_birth(self):
#         year=2023-self.age
#         return f"hello{self.name}you were born in {year}"
# #  class Vehicle:
#     def _init__(self,max_speed,mileage):
#       self.max_speed=max_speed
#       self.mileage=mileage
# from django.template import engines


# class Student:
#     def __init__(self,first_name,last_name,age,country) :
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.country=country
#     def show_full_name(self):
            
#             return f"{self.first_name} {self.last_name}"
#     def year_of_birth(self):
#          year=2023-self.age
#          return year
#     def show_initails(self):
        
#          return f"{self.first_name[0]}.{self.last_name[0]}" 
# class Car:
#          model="nissan"
# def __init__(self,make,year):
#         self.make=make
#         self.year=year
# def accelerate(self):
#                return f"{self.make} benz is hooting"
# class Fruits:
        # vitamin="ascorbic"
        # def __init__(self,name,taste):
        #         self.name=name
        #         self.taste=taste
        # def count_uits(self): 
        #         return f"{self.name} is very delicious"      
                
              

# class Account:
#         name="accontname"
# def __init__(self,account_number,amount):
#         self.account_number
#         self.amount
# def count_money(self):
#         return f"{self.account_number}"

#           def __init__(self,name,country,unique_ingredients,preparation_time,cooking_method,nutritional_value) :
#          self.name=name
#          self.country=country
#          self.unique_ingredients=unique_ingredients
#          self.preparation_time=preparation_time
#          self.cooking_method=cooking_method
#          self.nutritional_value=nutritional_value
# class MoroccanRecipe(Recipe):
#     def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
#         super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
#     def cook(self):
#         return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
# class EthopianRecipe(Recipe):
#     def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
#         super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
#     def cook(self):
#         return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at  {self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
# class  NigerianRecipe(Recipe):
#     def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
#         super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
#     def cook(self):
#         return f"for{self.name} of country  {self.country}  cook the meal with{self.ingredients} and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
# # morrocan= MoroccanRecipe("Wheat","Morrocco",[Maji,skuma],"30 minutes","grilling","500gms","cumin")
# # ethopian= EthiopianRecipe("chicken_breasts","Ethopia",[anjera,milk],"45 minutes","stewing","600gms","doro wat")
# nigerian=NigerianRecipe("Jollo Rice","Nigeria",["rice","tomato","onion"],"1 hour","cooking","700gms","party jollof")
# # print(morrocan.cook())
# # print(ethiopian.cook())
# print(nigerian.cook())



class Recipe:
     def __init__(self,name,country,unique_ingredients,preparation_time,cooking_method,nutritional_value) :
         self.name=name
         self.country=country
         self.unique_ingredients=unique_ingredients
         self.preparation_time=preparation_time
         self.cooking_method=cooking_method
         self.nutritional_value=nutritional_value
class MoroccanRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
class EthopianRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with and prepare at  {self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
class  NigerianRecipe(Recipe):
    def __init__(self, name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value):
        super().__init__(name, country, unique_ingredients, preparation_time, cooking_method, nutritional_value)
    def cook(self):
        return f"for{self.name} of country  {self.country}  cook the meal with and prepare at{self.preparation_time} using method{self.cooking_method}to gain  nutritional_value{self.nutritional_value}"
# morrocan= MoroccanRecipe("Wheat","Morrocco",[Maji,skuma],"30 minutes","grilling","500gms","cumin")
# ethopian= EthiopianRecipe("chicken_breasts","Ethopia",[anjera,milk],"45 minutes","stewing","600gms","doro wat")
nigerian=NigerianRecipe("Jollof","Nigeria","pepper","3hours","stiring","proteins")
print(nigerian.cook())

        
    
      
        
        


