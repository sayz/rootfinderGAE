#!/usr/bin/env python2.7
#-*-coding:utf-8-*-
'''
Created on 22 Mar 2013

@author: sayz
'''

from Bisection import bisection
from Parser import parse_string

import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

    title = "Bisection method"
    formstring = '''<form method="post" action="/">
                <p>Enter Function : <input type="text" name="fun"/></p>
                <p>Enter X1 (0):    <input type="text" name="x1"/></p>
                <p>Enter X2 (1): <input type="text" name="x2"/></p>
                <p>Enter Epsilon: <input type="text" name="ep"/></p>
                <p><input type="submit" value= "Hesapla"></p>
                <h4>Demos:</h4>
                <ul>
                  <li>x^3 - 10x^2 + 5</li>
                  <li>x1 = 0, x2 = 1</li>
                </ul>
                <ul>
                  <li>x^3 + 4x^2 - 1</li>
                  <li>x1 = 0, x2 = 1</li>
                </ul>
                <ul>
                  <li>x^3 + 4x^2 - 10</li>
                  <li>x1 = 1, x2 = 2</li>
                </ul>
                <ul>
                  <li>x^3 - x - 3</li>
                  <li>x1 = 1, x2 = 2</li>
                </ul>
                </form>'''

    def fx(self, x, coef_list):
        result = 0
        for j in range(len(coef_list)):
            result += coef_list[len(coef_list) - (j + 1)] * \
                                x ** (len(coef_list) - (j + 1))
        return result

    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write("""<html>
                                <head>
                                    <title>""" + self.title + """</title>
                                    <meta http-equiv="Content-Type" \
                                            content="text/html; charset=UTF-8">
                            </head>
                            <body BGCOLOR=#A7A7A7>""")

            self.response.out.write('<h2>Bisection method</h2>')

            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

        self.response.out.write(self.formstring)
        self.response.out.write("<h2 align='right'>by Sayz</h2>")
        self.response.out.write('</body></html>')

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("""<html>
                                <head>
                                    <title>""" + self.title + """</title>
                                    <meta http-equiv="Content-Type" \
                                            content="text/html; charset=UTF-8">
                            </head>
                            <body BGCOLOR=#A7A7A7>""")
        fun = self.request.get('fun')
        epsilon = self.request.get('ep')

        coef_list = parse_string(fun)

        x1 = self.request.get('x1')
        x2 = self.request.get('x2')

        x1 = float(x1)
        x2 = float(x2)
        bid = bisection(self.fx, coef_list, x1, x2, float(epsilon))

        for xfe in range(len(bid[1])):
            self.response.out.write('<p>' + '=' * 5 + str(xfe + 1) +
                    '. deneme' + '=' * 5)
            self.response.out.write('<p> x1: %2.5f, x2: %2.5f </p>' %
                                    (bid[1][xfe][0], bid[1][xfe][1]))
            self.response.out.write('<p> f(x1): %2.5f, f(x2): %2.5f </p>' %
                                    (bid[2][xfe][0], bid[2][xfe][1]))
            self.response.out.write('<p>bu deneme için hata payı: %1.10f</p>'
                                    % bid[3][xfe])

        self.response.out.write('<br><br><br>**********SONUÇLAR**********<br>')
        self.response.out.write('<br>' + str(xfe + 1) +
                ' adımda çözüme ulaşıldı.<br><br>')
        self.response.out.write('verilen fonksiyon: ' + fun + '<br>')
        self.response.out.write('<p>son hata payı: %1.10f  < %1.5f (ε) </p>' %
                                (bid[3][xfe + 1], float(epsilon)))
        self.response.out.write("""
        ============================================ <br>
        Kök ~= """ + str(bid[0]) + """<br>
        ============================================
        """)

        self.response.out.write("<h2 align='right'>by Sayz</h2>")
        self.response.out.write('</body></html>')


def main():
    application = webapp.WSGIApplication([
                                          ('/.*', MainHandler)],
                                         debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
