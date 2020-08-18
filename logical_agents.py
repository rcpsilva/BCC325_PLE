class LogicalAgent():

    def __init__(self,KB):
        self.KB = KB

    # TODO
    def top_down(self,query,indent=''):
        pass
    
    # TODO
    def bottom_up(self):
        pass

    def explain(self,g,assumed = set()):
    
        if g:
            selected = g[0]
            if selected in self.KB.assumables:
                return self.explain(g[1:],assumed|{selected})
            else:
                return [a 
                        for cl in self.KB.clauses_for_atom(selected)
                        for a in self.explain(cl.body+g[1:],assumed)
                        ]
                       
        return [assumed]


def yes(ans):
  return ans.lower() in ['yes','yes.','y','y.','sim','sim.','s','s.']

def ask_askables(kb):
  return [at.atom for at in kb.askables if yes(input('Is ' + at.atom + ' true?'))]