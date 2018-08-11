**1.Page design**
/
index
 nothing,only show a blank(no need login)

/recruit?suid=xxxx-xx-xx-xxxx
 a sign up page(no need login)
 
/results?suid=xxxx-xx-xx-xxxx
 sign up result(maybe need cookie support)(no need login)
 
/backoffice
/login
/backoffice/student
/backoffice/recruit
/backoffice/depart
 login page
 
/backoffice/recruit/list
/backoffice/recruit/add
/backoffice/recruit/modify?suid=xxxx-xx-xx-xxxx
/backoffice/recruit/detail?suid=xxxx-xx-xx-xxxx
/backoffice/student/add?suid=xxxx-xx-xx-xxxx
/backoffice/student/detail?suid=xxxx-xx-xx-xxxx&stid=xxxx-xx-xx-xxxx
/backoffice/depart/add
/backoffice/depart/list
/backoffice/depart/modify?dtid=xxxx-xx-xx-xxxx
 recruit mgnt page,depart mgnt page and student mgnt page,need login
 
**2.table design**
students:
 id:id(table key)
 name:vchar(10)
 gender:char(10)(female/male)
 nation:char(10)
 id_number:char(20)
 parent_name:vchar(10)
 telephone_number:char(20)
 target_depart:id(table departs)
 recruit_id=id(table recruits)
 from=char(10)(front/back)
 recruit_result=char(10)(succ/fail)

recruits:
 id:id
 name:vchar(30)
 start_time:date
 ended_time:date
 show_result_start_time:date
 allowed_earliest_birthday:date
 allowed_latest_birthday:date
 uuid:char(100)(table key)
 enabled:char(10)(true/false)
 introduce:vchar(2000)
 succ_info:vchar(2000)
 wait_result_info:vchar(2000)

scales:
  id:id
  recruit_id:id(table recruits)
  depart_id:id(table departs)
  scale:int
  
departs:
  id:id 
  name:vchar(100)
  intro:vchar(1000)
  address:vchar(100)
 
**3.object design**
student:
  public string id = ""
  public string name = ""
  public string gender = ""
  public string nation = ""
  public string id_number = ""
  public string parent_name = ""
  public string telephone_number = ""
  public boolean recruit_result = False
  public recruit_id = "" #recruit's id in table recruits
  public string from = ""
  public string target_depart = "" #depart's id in table depart
recruit:
  public string id = ""
  public string name = ""
  public string introduce = ""
  public string succ_info = ""
  public string wait_result_info = ""
  public DateTime start_time = None
  public DateTime ended_time = None
  public DateTime show_result_start_time = None
  public DateTime allowed_earliest_birthday = None
  public DateTime allowed_latest_birthday = None
  public string uuid = ""
  public boolean enabled = False
  public arrary scale = [object scale]
  public arrary depart = [object depart]
scale:
  public string id = ""
  public string recruit_id = ""
  public string depart_id = ""
  public int scale = ""
depart:
  public string id = ""
  public string name = ""
  public string intro = ""
  public string address = ""


**logic**
recruit show logic:
[added,enabled,it's not start time] /recruit:show introdu,can't sign up;/results redirect to /recruit page.
[added,enabled,it's signup's time]   /recruit:allow sign up,and show sign up results;/results redirect to /recruit page.
[added,enabled,it's show result time] /recruit:redirect to /results page;/results show results.
[added,enabled,it's ended time but not show result time.] /recruit&/results:show "Please wait for results" page.
[added,disabled] /recruit:404;/results:404
recruit operation logic:
add->list
     modify
     delete
     [enabled/disabled]
students operation logic in backoffice:
add->list
     modify
     delete
