class Category:
    def __init__(self, category=""):
        self.funds = 0
        self.ledger = []
        self.category = category
        self.spent = 0

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount, description=""):
      if self.check_funds(amount) == True:
          self.ledger.append({"amount": -amount, "description": description})
          self.funds -= amount
          self.spent += amount
          return True
      else:
          return False

    def get_balance(self):
        return self.funds

    def transfer(self, amount, category2):
        if self.check_funds(amount) == False:
          return False
        else:
          self.withdraw(amount, f"Transfer to {category2.category}")
          category2.deposit(amount, f"Transfer from {self.category}")
          return True

    def __str__(self):
         title = self.category.center(30, "*") + "\n"
         for item in self.ledger:
            title += item["description"][0:23].ljust(23)
            title += f'{float(item["amount"]):.2f}'.rjust(7) + "\n"
         return f"{title}Total: {self.funds:.2f}"

def create_spend_chart(categories):
    num_categories = len(categories)
    line_title = "Percentage spent by category\n"
    chart_lines = ["  0|", " 10|" ," 20|", " 30|", " 40|", " 50|", " 60|", " 70|", " 80|", " 90|", "100|"]
    horz_line = "    " + "---"*num_categories + "-\n"
    axis_title = "    "
    split_title = []
    split_words = []
    total_w = 0
    for i in categories:
      total_w += i.spent
    for item in categories:
      nbars = round((item.spent/total_w)*100)/10
      for reps in range(11):
        if nbars >= reps:
            chart_lines[reps] += " o "
        else:
            chart_lines[reps] += "   "
      split_title.append(item.category)
    chart_lines.reverse()
    for line in chart_lines:
        line_title += line + " \n"
        
  #bar titles
    for i in split_title:
        i = i.capitalize()
        sub_split_words = []
        for number in range(len(i)):
            sub_split_words.append(i[number])
        split_words.append(sub_split_words)
    number_flines = len(max(split_title, key=len))
    
    for reps in range(number_flines):
        for x in split_words:
            if reps < len(x):
                axis_title += f' {x[reps]} '
            else:
                axis_title += "   "
        if reps < number_flines-1:
          axis_title += " \n    "
        else:
          axis_title += " "
    spend_chart = line_title + horz_line + axis_title
    return spend_chart
  
