# @Author: genli
# @Date:   2020-01-13T12:10:59-05:00
# @Last modified by:   genli
# @Last modified time: 2020-01-14T19:53:32-05:00


import pandas as pd
import smtplib, ssl
import os
import time
import schedule
import getpass


class check_gradcafe:

    def __init__(self, major, sender_email, password, receiver_email):
        self.major = major
        self.url = "https://www.thegradcafe.com/survey/index.php?q=" + self.major

        self.port = 465  # For SSL
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.context = ssl.create_default_context()


        df = pd.read_html(self.url)[0]
        self.inst_last = df.Institution[0]
        self.date_add_last = df["Date Added"][0]

        self.message = """\
        Subject: Begin to check GradCafe

        A checking work is successfully initiated! """

        print("A checking work is successfully initiated!")

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.message)


    def check(self):
        df = pd.read_html(self.url)[0]
        if (self.inst_last != df.Institution[0]) & (self.date_add_last != df["Date Added"][0]):
            self.inst_last = df.Institution[0]
            self.date_add_last = df["Date Added"][0]

            message = """\
            Subject: New Post

            New post for """ + self.major + """ program comes out.

            Institution: """ + self.inst_last + """, Program: """ + df["Program (Season)"][0]

            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, self.receiver_email, message)

            print("New message is sent.")



if __name__ == "__main__":
    print("""\
    *************************************************************************************************
             .   .    .   .   .    .   .        .                    l$$               .        . .
       $$$$$$$i          .     .      .     . .    .       .     $$   $$                     $
       $$    $$$                                                $      $                   ?$
       $$..   $$    .  .         .  .                  .       $$ . .          .          .$..
       $$     .$$          .                          .        $   .    ^       .   .     $$     .
    .  $$      $$.       .    .   .   .  .     .   .  "  '    $$                       .  $
       $$      Q$Z  $ .$$  $$ $$$$ . $  $i   $  $$  r$$ $$$   $$            Q$ $$        $$  _
       $$     . $$ $$  $$  .$   W$   #   i  $j   $   $$$  $0  $$   .        $   $$  .    $$$$$$  .
       $$       $$ $$   $   $'   $. !$   i  $ .. $$  $$   $$  $$      $$$  $$    $       $$   $$
       $$       $$     m$   $    $   $$    _$    $$  $$ . $$. $$       $$. $|    $$   .  $    $$
     . $$      ^$k.   $ $   $    $   $$$   $$    L$ .$$   $$  $$ .     $$  $;    $$     .$     $
       $$      $$   $ . $   $    $ .  $$$  $$   . $  $$   $$. $$       $$. $C    $$   .  $     $
      .$$     .$$  $$   $  .$    $     l$$ $$     $  $$   $$  $$       $$  $$    $$ .    $!    $ .
       $$     8$.  $j   $  .$    $.     c$  $" . @$  $$   $$   $$      $$  $$    $  .    $$    $ .
       $$   . $$.  $$  $$   $.   $       $. $$   ${  $$   $$   $$    . $$  o$    $.       $   u$
       $$j  $$$    $$$$ $$  $B   $   $  *$   $`  $  .$$   $$    $$r   B$0   $$  $         $$  $
     $$$$$$w        $$  $  $$$$@$$$$ j$$B     $$$   $$$$ $$$$     $$$$$      $$$           $$$

                                            :...
                                           ZCCC`.                 '
                                          )C|tOZ'....  .      ..QCQ>'
                                          Q0tt/mLLCQQLJLn'    YQmfQC.
                                      .^UQLtttttfjjftf\)JZCLCCL\fO\Lf
                                    .xQCOtf/ttttttttttttttttfftftt/JQ.
                                  .xLCvfttttttttttttttttttttttttftf\CJ:.
                                .`JL\/tt//ttfttvxctttttttttttttttttttfZJ.
                              '`0Qmttttt/???-\fnntttt/jttj/ttttttttttttmL'
                              .CL|fftttt]]???_ftfttttf]--][ttttttttttttj0J.
                             ^Q0_."ftt)@@$f}-?f/tttf)]-]?-+tttttttttttttjJf
                            '0O.  `^j$"C$B$@1}ttt/t[_)jt@%%@rt/tttttttttt/C`.
                            LC'.  .tf^ $@$$%\/ttttt/fuB `%@@@$/ttttttttttf0C.
                          ."C{    'ffa`'%B@ftttttttf@   @@@@@$Bttffttttttt|Q
                          .LO^    .]/t<YCm/ftttttttt\c&. @@@@@/ttttttttttttQ^
                           LL     .."tt(Xc(\tttttttttj|/)fY1x\///.'tttttt/fQ"
                          .QI        Q@$$$$$B_t/tr(` .)//ttt/jt ...(ftttttt0(
                          'L`.       .$l_$$$$$ .       ^'..'`      }rttttttCY
                          .Q;.        $$$@%$$.  `                .'\fttttttCL
                          .Qc        )+<>#$-.                    ^?ttttttt/LU
                          .LU.       ;%i<_<<<'    .              .-\tttttt/Cf
                          .^C`         <!j$B\>+>$>                  . ^.|t/Q:
                            JQ.^            .                           jfZL'
                            .L0t`                                      .ffLQ.
                              0L/t'"..                                 "t\C^.
                              '.CCut!. " '                            .tt(L'
                              jC0'"J0j/fi.                           `rtt|C.
                            LQzL^.^tttL^ `""...                     ^ttttjL
                        .'.Ynf/t.'r/ttf`'  ...            ''`"^^.     \tt0Q
                       .ZLCZ/ftt^ fjttttx?'^CC^.   '..`r`. .."..(m.  .\ffL]
                      'QmfJttttt/.Q|tttttttttt\OJ,"JCffttttttttf/~I![|ftqJ.
                    'iQ0ffJ1fttt\/Qftttttttttt//0L.'^vrtttttttttttttttt(O'
                    .C0/ffnC/ftt0LQ|tttttttttt/cQ  . '`ttttttttttttttttQ^
                      ';QLCQ/  ,^'UCjtttttttttjC"x"   .ttf\/fttttttt/JU`.
                           .QL"`'UCLCQ0/ffftttfCL`I``)`000UCLLc//|0CQ'.
                             `':`^.   ^ULQCCCLQJLCQ0JO`'. O .^`xLx^.
                                                 uC'.'".'`Qc
                                                  .QJm`m.UZ`
                                                   '.`:x)`


     ================================
     Version: 0.01
     Created: 2020/01/13

     Author: Gen Li
     Web: https:///www.gen-li.com
     ================================

     Instruction:
     The program can keep tracking new admission results on GradCafe at a specified frequency
     (e.g., 5 mins). It will send you an email and let you know if there is an update on the
     application results.

     Before you use the program, you need to set up the email accounts that will send and receive
     updates. I suggest you use Gmail as the sender email account. Before you set up the sender email,
     you need to go to https://myaccount.google.com/lesssecureapps and turn Allow less secure apps
     to ON for the sender account. There is no requirement for the receiver.

     The program is still at early stage and may contain many errors. Welcome to fork and pull request
     from github to make it better.


    *************************************************************************************************



    """)
    major = input("Type the major you want to track and press enter: ")
    sender_email = input("Type your sender email account and press enter: ")
    password = getpass.getpass("Type your password and press enter: ")
    receiver_email = input("Type your receiver email account and press enter: ")
    freq = input("Type the checking frequency and press enter (e.g., type '5' to check every 5 minutes): ")

    check = check_gradcafe(major, sender_email, password, receiver_email)

    schedule.every(int(freq)).minutes.do(check.check)
    while True:
        schedule.run_pending()
        time.sleep(1)
