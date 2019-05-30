#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Базовый класс компонента
class Component():
    
    def execute(self) -> str:
        pass


#Класс конкретного компонента, который предосталвяет реализацию по умолчанию
class ConcComponent(Component):
    
    def execute(self) -> str:
        return "Inner core of Earth"


class BaseDecorator(Component):
    
    wrappee: Component = None

    def __init__(self, c: Component) -> None:
        self.wrappee = c

    @property
    def component(self) -> str:
        return self.wrappee

    def execute(self) -> str:
        self.wrappee.execute()

#Создание конткретных декораторов, которые добавляют свойства объекту
class ConcDecorator1(BaseDecorator):

    def execute(self) -> str:
        return f"Outer core({self.component.execute()})"


class ConcDecorator2(BaseDecorator):

    def execute(self) -> str:
        return f"Mantle({self.component.execute()})"
    
class ConcDecorator3(BaseDecorator):
    
    def execute(self) -> str:
        return f"Crust({self.component.execute()})"
    
class ConcDecorator4(BaseDecorator):
    
    def execute(self) -> str:
        return f"Lithosphere({self.component.execute()})"
    
class ConcDecorator5(BaseDecorator):
    
    def execute(self) -> str:
        return f"Atmosphere({self.component.execute()})"


#Функция для работы со всеми объектами
def printComponent(component: Component) -> None:
    print(f"Component: {component.execute()}", end="")



if __name__ == "__main__":
    # Создание простого компонента
    component = ConcComponent()
    print("Component without decorators: ")
    printComponent(component)
    print("\n")

    #Обертка компонента декораторами
    decorator1 = ConcDecorator1(component)
    decorator2 = ConcDecorator2(decorator1)
    decorator3 = ConcDecorator3(decorator2)
    print("Component with some decorators: ")
    printComponent(decorator3)
    print("\n")
    
    decorator4 = ConcDecorator4(decorator3)
    decorator5 = ConcDecorator5(decorator4)
    print("Let's finish our Earth: ")
    printComponent(decorator5)
    

