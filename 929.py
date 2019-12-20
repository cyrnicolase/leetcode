

class Solution:
    def numUniqueEmails(self, emails):
        result = {}
        count = len(emails)
        for i in range(count):
            email = emails[i]
            at = email.find("@")
            domain = email[at:]
            name = email[:at]

            plus = name.find("+")
            if -1 != plus :
                name = name[:plus]
            
            name = name.replace(".", "")
            
            email = name + domain
            result[email] = 1

        return len(result)

solution = Solution()
print(solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))