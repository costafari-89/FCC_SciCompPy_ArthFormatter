def arithmetic_arranger(problems, show_answers=False):

    def str_builder(i_num, num_1, num_2, op):

        
        if op == "+":
            solution = int(num_1) + int(num_2) 
        else:
            solution = int(num_1) - int(num_2)

        sol_len = len(str(solution))
        bop_len = len(num_1)
        aop_len = len(num_2)

        max_num_len = max(bop_len, aop_len)
        width = max_num_len + 2

        top_row = (width - bop_len) * ' ' + str(num_1)
        mid_row = op + ' ' + ((width - aop_len - 2) * ' ') + str(num_2)
        bott_row = '-'*width
        sol_row = (width - sol_len) * ' ' + str(solution)

        if i_num != 0:
            
            top_row = (' ' * 4) + top_row
            mid_row = (' ' * 4) + mid_row
            bott_row = (' ' * 4) + bott_row
            sol_row = (' ' * 4) + sol_row
        
        return top_row, mid_row, bott_row, sol_row

    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        first_line=""
        second_line=""
        seperator=""
        solution=""
        for i, eq in enumerate(problems):
            if "+" in eq:
                # print("addition")
                # print(eq)
                [before_op, after_op] = eq.split('+')
                before_op = before_op.strip()
                after_op = after_op.strip()

                if len(before_op) > 4 or len(after_op) > 4:
                    return 'Error: Numbers cannot be more than four digits.'

                elif not (before_op.isnumeric() and after_op.isnumeric()):                
                    return 'Error: Numbers must only contain digits.'
                else:
                    
                    top_row, mid_row, bott_row, sol_row = str_builder(i, before_op, after_op, '+')
                
                    first_line += top_row
                    second_line += mid_row
                    seperator += bott_row
                    solution += sol_row

                # bop_len = len(before_op) 
                # aop_len = len(after_op)
                # max_num_len = max(bop_len, aop_len)
                # width = max_num_len + 2
                
                # if i > 0:
                #     first_line += '    ' + (width - bop_len) * ' ' + str(before_op)
                #     second_line += '    ' + '+ ' + ((width - aop_len - 2) * ' ') + str(after_op)
                #     seperator += '    ' + '-'*width
                # else:
                #     first_line += (width - bop_len) * ' ' + str(before_op)
                #     second_line += '+ ' + ((width - aop_len - 2) * ' ') + str(after_op)
                #     seperator += '-'*width


            elif "-" in eq:
                # print("subtraction")
                # print(eq)

                [before_op, after_op] = eq.split('-')
                before_op = before_op.strip()
                after_op = after_op.strip()

                if len(before_op) > 4 or len(after_op) > 4:
                    return 'Error: Numbers cannot be more than four digits.'

                elif not (before_op.isnumeric() and after_op.isnumeric()):                
                    return 'Error: Numbers must only contain digits.'
                else: 
                    
                    top_row, mid_row, bott_row, sol_row = str_builder(i, before_op, after_op, '-')
                
                    first_line += top_row
                    second_line += mid_row
                    seperator += bott_row
                    solution += sol_row

            else:
                return "Error: Operator must be '+' or '-'."
        true_list = [first_line, second_line, seperator,solution]
        false_list = [first_line, second_line, seperator]
        
        # print('The first line is:', first_line)
        # print('The secon line is:', second_line)
        # print('The third line is:', seperator)
        # print('\n'.join(string_list))
        if show_answers:
            return '\n'.join(true_list)
        else:
            return '\n'.join(false_list)
    



print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
 