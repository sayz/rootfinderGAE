#!/usr/bin/env python2.7
#-*-coding:utf-8-*-

'''
Created on 25 Mar 2013

@author: sayz
'''

from Parser import parse_string


def isZero(n):
    if bool(n): return n


def bisection(f, lis, x1=0, x2=1):
    f1 = f(x1, lis)  # f(x1), f(x2) hesaplanıyor.
    isZero(f1)

    f2 = f(x2, lis)
    isZero(f2)
    print "\n============= 1. deneme ==========\n"
    print "x1: %2.5f, x2: %2.5f" % (x1, x2)
    print "f(x1): %2.5f, f(x2): %2.5f\n" % (f1, f2)
    print "bu deneme için hata payı: %1.10f\n" % ((x2 - x1) / 2.0)

    if f1 * f2 > 0.0:  # f(x1) x f(x2) < 0 kontrolü yapılıyor
        print 'Root is not bracketed'
    else:
        ep = 0.0000000000000000000000001  # epsilon
        i = 0
        while (((x2 - x1) / (2.0 ** (i + 2))) > ep):  # hata < ep kontrolü
            print "========== " + str(i + 2) + ". deneme ==========\n"
            x3 = (x1 + x2) * 0.5
            f3 = f(x3, lis)  # f(x3) hesaplanıyor

            if (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
                return None

            isZero(f3)

            if f2 * f3 < 0.0:
                x1 = x3
                f1 = f3
            else:
                x2 = x3
                f2 = f3

            print "x1:     %2.5f, x2:     %2.5f" % (x1, x2)
            print "----------------------------"
            print "f(x1): %2.5f, f(x2): %2.5f\n" % (f1, f2)
            print "bu deneme için hata payı: %1.10f\n" \
                                % (float((x2 - x1) / (2 ** (i + 2))))
            i += 1

        print "epsilondan kucuk olan hata payi %1.10f\n" \
                            % (float((x2 - x1) / (2 ** (i + 2))))
        print f1, f2
        return (x1 + x2) / 2.0


def fx(x, coef_list):
    result = 0
    for j in range(len(coef_list)):
        result += coef_list[len(coef_list) - (j + 1)] * \
                            x ** (len(coef_list) - (j + 1))
    return result


def gx(x):
    pass

kat_list = parse_string("x^3 - 8")
kok = bisection(fx, kat_list, 1.0, 2.1)

print "------------------------------------------------------\nkökümüz de \
yaklaşık olarak şöyle bi şey: %2.15f" % kok

print "===================="
