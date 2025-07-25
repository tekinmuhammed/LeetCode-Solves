class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res