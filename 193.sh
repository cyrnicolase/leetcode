# https://leetcode.com/problems/valid-phone-numbers/description/


sed -nr '/(^[0-9]{3}-|^\([0-9]{3}\)\s)[0-9]{3}-[0-9]{4}$/p' file.txt
