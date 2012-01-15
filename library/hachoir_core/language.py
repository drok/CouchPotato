from hachoir_core.iso639 import ISO639_1,ISO639_2

class Language:
    def __init__(self, code):
        code = str(code)
        if len(code) == 2:
          if code not in ISO639_1:
            raise ValueError("Invalid language code: %r" % code)
        else:
          if code not in ISO639_2:
            raise ValueError("Invalid language code: %r" % code)
        self.code = code

    def __cmp__(self, other):
        if other.__class__ != Language:
            return 1
        return cmp(self.__unicode__(), other.__unicode__())

    def __unicode__(self):
       if len(self.code) == 2:
          return ISO639_1[self.code]
       else:
          return ISO639_2[self.code]

    def __str__(self):
       return self.__unicode__()

    def __repr__(self):
        return "<Language '%s', code=%r>" % (unicode(self), self.code)

