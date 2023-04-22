from logical_prediction import gr


def findbiggestfact(x):

    r = 0

    for i in range(1,x):

        if x % i == 0:

            r = i

    return r



def calc(formula, env):

    """if env == format(57, "b").zfill(l):


        print(formula, env,format(findbiggestfact(57), "b").zfill(l) , "\n")"""



    for clause in formula:

        res = True

        for element in clause:

            if (element[-1] == "+") != (env[int(element[:-1])] == "1"):

                res = False

        if res:

            return res

    return False


class Digit:
    def __init__(self, numb, l):
        self.pos = ""

        self.numb = numb


    def commit(self, sample):

        self.pos = self.pos + str(sample) + " "



    def formulate(self):

        if self.pos == "":

            return False
        self.formula = gr(self.pos, "")


    def test(self, subject):

        if self.pos == "":

            return False


        return calc(self.formula,subject)


if __name__ == "__main__":

    l = 8

    db = []



    for i in range(l):

        db.append(Digit(i, l))

    for i in range(2**(l)):

        for dig in range(len(db)):



            if format(findbiggestfact(i), "b").zfill(l)[dig] == "1":

                db[dig].commit(str(int(format(i, "b").zfill(l), 2)))

    for i in db:
        print()
        print(i.pos)
        i.formulate()


    for t in range(2**(l)):
        biggestfac = ""

        test = format(t, "b").zfill(l)

        for i in db:

            if i.test(test):

                biggestfac = biggestfac + "1"

            else:
                biggestfac = biggestfac + "0"

        if format(findbiggestfact(t), "b").zfill(l) != biggestfac:

            print(format(findbiggestfact(t), "b").zfill(l), biggestfac)







