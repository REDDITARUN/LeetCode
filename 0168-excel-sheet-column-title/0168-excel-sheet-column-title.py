class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        al = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        lett = al.split(' ')
        res = []
        
        
        while columnNumber>0:
            columnNumber -=1
            
            remainder = columnNumber % 26
            res.append(lett[remainder])
            
            columnNumber = columnNumber // 26
            
        return ''.join(res[::-1])
            
            
        