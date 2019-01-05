"""This class is used for expression evaluation
    Developed for: Payroll rest project
    Developed on : 01-04-2019
    Developed by: Sahariar Alam Khandoker
"""
class ExpressionEvaluation:


    def evaluate(self,tokens):
        return self.postfix_evaluation(self.infix_to_postfix(tokens))
    def infix_to_postfix(self,tokens):
        postfix=[]
        stack=[]

        for token in tokens:
            print(stack)
            if(self.isOperator(token)):
               if (token == '('):
                    stack.append(token)
               elif (token == ')'):
                    while len(stack) != 0 and (self.stack_peek(stack) != '('):
                        postfix.append(stack.pop())
                    stack.pop()
               elif(len(stack)==0 or self.token_precendence_is_gt_stack_top_element(token,stack)):
                   print("token is {a}".format(a=token))
                   stack.append(token)
               else:
                   print("token is {a}aa".format(a=token))
                   while len(stack)!=0 and not self.token_precendence_is_gt_stack_top_element(token,stack):
                        postfix.append(stack.pop())
                   stack.append(token)

            else:
                postfix.append(token)

        while len(stack) !=0:
             postfix.append(stack.pop())
        print(postfix)
        #self.postfix_evaluation(postfix)
        return postfix

    def isOperator(self,token):

        if(token=='+' or token =='-' or token=='*' or token == '/' or token =='(' or token==')'):
            return True
        else:
            return False

    def stack_peek(self,stack):
        return stack[len(stack)-1]

    def token_precendence_is_gt_stack_top_element(self,token,stack):
        stack_top=self.stack_peek(stack)
        precendence_map={
            '*':3,
            '/':3,
            '+':1,
            '-':1,
            '(':-1

        }
        if(precendence_map[token]>precendence_map[stack_top]):
            return True
        else:
            return False


    def postfix_evaluation(self,postfixtokens):
        stack=[]
        for token in postfixtokens:
            if(not self.isOperator(token)):
                stack.append(token)
            else:
                operandb=float(stack.pop())
                operanda=float(stack.pop())
                op=0;
                if(token=='+'):
                    op=operanda+operandb
                elif(token=='-'):
                    op=operanda-operandb
                elif(token=='*'):
                    op=operanda*operandb
                elif(token=='/'):
                    if(operanda!=0):
                        op=operanda/operandb

                stack.append(op)

        answer=stack.pop()
        print(answer)
        return answer


