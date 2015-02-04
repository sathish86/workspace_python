class GameEntry():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return "{0}:{1}".format(self.name,self.score)


#obj = GameEntry("sathish",100)


class ScoreBoard():
    def __init__(self):
        self.board = [None] * 10
        self.counter = 0
        
    def __getitem__(self,):
        
        
    def add_entry(self,kwargs):
        good = self.counter > len(self.board) or kwargs['score'] > self.board[-1].get_score()  
        
        
        if good:    
            game_obj = GameEntry(**kwargs)
            self.board[self.counter] = game_obj
            self.counter += 1
            
        
    def __str__(self):
        import pdb; pdb.set_trace()
        
        return "\n".join(str(i) for i in self.board)
        #return s
        
obj = ScoreBoard()
obj.add_entry({'name':"bala", 'score':100})
obj.add_entry({'name':"Kumar", 'score':200})
obj.add_entry({'name':"Kumar", 'score':200})

print str(obj)