# coding: utf-8
#                                                    ##       ##
#                                                  #####   #  ####
#                                               ######### ## #######
#                                              ###  ############ ##
#                               ####          #     ####### #########
#  ###########               #########       #      ###########  ##
# #############             ###    ####        ##  #### ########                                     ##
# ##   ##    ##            ##        ###     #########  #########        ###         ##       #     ###      ##      #
#      ##   ##                    ## ###    ########   ##########       #### ##     ###     ####   ###    #####    ####
#     ## ####                     ##  ##   #########   ##########      ########    #####   ####    ####   #####   #####
#    ######          ####        ##   ##  ### ## ###  ############    ## ### ##   ## ##   ###      ###    #####  ### ##
#    ####           #####        ##  ###  ###  ###### ############       ##  ##  #####    ### ##  ###     ###    #####
#   ## ##         ### ###       ###  ###   ######### ##############     ### ##   ####     ## ###  #####  ####    ####
#   ## ###        ##  ##        ##  ###     #####    ##############    #######    #####   #####   #####  ###     ######
#  ##   ###  ##  #######        ######              ###############    ####         ##     ##       #              ###
#  ##   ######   #######       #####               #################   ###
# ##      ###     ##  ##       ###                  #################  ##
# ##                           ##                 ###################  ##
# ##                          ###                  ######################
#                             ##                    #               ## #
#                             ##
# author: RaPoSpectre
# time: 2016-11-12

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        letter_dict = {'2': ['a', 'b', 'c'],
                       '3': ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'],
                       '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'],
                       '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'],
                       '9': ['w', 'x', 'y', 'z']}
        letter_list = [letter_dict[i] for i in digits]
        res = letter_list[0]
        for i in xrange(1, len(letter_list)):
            res = self.kronecker(res, letter_list[i])
        return res

    def kronecker(self, ma, mb):
        res = []
        for a in ma:
            for b in mb:
                res.append('{0}{1}'.format(a, b))
        return res


# print Solution().letterCombinations('23235')
