class Article:

    all=[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
       
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed once it is set")
            print("Title cannot be changed once it is set")

        else:
            if isinstance(new_title, str):
                if len(new_title) >= 5 and len(new_title) <= 50:
                    self._title = new_title
                else:
                    raise ValueError("title MUST be btn 5 and 50 characters.")
                
            else:
                TypeError("Title MUST be a string")
            
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
           self._author = new_author 
        else:
            TypeError("author MUST be an instance of the Author class")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("magazine must be an instance of the Magazine class")




class Author:
    def __init__(self, name):
        self.name = name

    @property 
    def name (self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        # hasattr() checks for the presence of an attribute and returns true or false.
        if hasattr(self, "name"):
            AttributeError("Author can't be changed after it is set")
        
        else:
            # If the input is not a string, it should raise an error
            if isinstance(new_name, str):
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
         # If the input is empty(less than one character) it should raise an error
                if len(new_name) > 0:
                    self._name = new_name
                else:
                    raise ValueError("Please insert a name")
            else:
                TypeError("name MUST be a string")
                

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        # Getting all articles
        articles = self.articles()

        # Creating an empty set to store unique magazine names
        unique_magazines = set()

        for article in articles:
            magazine_name = article.magazine
            # Adding the magazine name to the set
            unique_magazines.add(magazine_name)

        # Converting the set to a list
        mag_list = list(unique_magazines)

        return mag_list


    def add_article(self, magazine, title):
        article = Article(self,magazine,title)
        return article

    def topic_areas(self):
        # Getting all the categories from magazines
        mag_categories =[x.category for x in self.magazines()]

        # creating a set to remove duplicates
        unique_mag = set(mag_categories)

        # Converting the set to a list
        unique_list = list(unique_mag)

        # If the author has contributed, return true
        if unique_list == True:
            return unique_list
        # If there are no articles, return None
        else:
            return None
    
   

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
         # If the input is not a string, it should raise an error
        if isinstance(new_name, str):
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        # If the input's length isn't between 2 and 16 chars, raise an error
            if len(new_name) >= 2 and len(new_name) <= 16:
                 self._name = new_name
            else:
                raise ValueError("name MUST be btn 2 and 16 characters")
        else:
            TypeError("name MUST be a string")
    
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        # If the input is not a string, it should raise an error
        if isinstance(new_category, str):
            # If the input is empty(less than one character) it should raise an error
            if len(new_category) > 0:
                 self._category = new_category
            else:
                raise ValueError("Please input a category")
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        else:
            TypeError("Category MUST be a string!!")
        

    def articles(self):
        the_articles =[]
        for article in Article.all:
            if self == article.magazine:
                the_articles.append(article)
        return the_articles

    def contributors(self):
        # An empty set that will hold unique authors
        unique_authors = set()

        for x in self.articles():
            # Adding the author to the set
            unique_authors.add(x.author)
        
        # Converting the st to a list
        auth_list = list(unique_authors)

        return auth_list

    def article_titles(self):
        list_of_titles = [{x.title for x in self.articles()}]
        if list_of_titles == True:
            return list_of_titles
        else:
            return None

    def contributing_authors(self):
        pass


author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")
author_1.add_article(magazine_1, "How to wear a tutu with style")
author_1.add_article(magazine_2, "Carrara Marble is so 2020")
author_2.add_article(magazine_2, "2023 Eccentric Design Trends")


print(f"{author_1.name}'s Articles: {[article.title for article in author_2.articles()]}")
print(f"{author_2.name}'s Articles: {[article.title for article in author_2.articles()]}")
print(f"{author_1.name}'s Magazines: {[magazine.name for magazine in author_2.magazines()]}")
print(f"{author_2.name}'s Magazines: {[magazine.name for magazine in author_2.magazines()]}")
print(f"{author_1.name}'s Topic Areas: {author_2.topic_areas()}")
print(f"Articles in {magazine_1.name}: {[article.title for article in magazine_1.articles()]}")
print(f"Article Titles in {magazine_2.name}: {[article.title for article in magazine_2.articles()]}")
