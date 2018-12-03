#! python3
# -*- encoding: utf-8 -*-
'''
Current module: rman.httptest.models

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:     luokefeng@163.com
    RCS:      rman.httptest.models,  v1.0 2018年11月22日
    FROM:   2018年11月22日
********************************************************************
======================================================================

Provide a function for the automation test

'''

from rman import db
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime
    
class Case(db.Model):
    ''' 测试用例   -> 所有的测试用例    '''
    __tablename__ = 'case'
        
    id              = Column(Integer, primary_key=True)
    project_id      = Column(Integer, nullable = False, comment = '关联的项目ID')
    desc            = Column(String(64), comment = '用例的简单描述')
    name            = Column(String(32), nullable = False, comment = '测试用例名称')
    responsible     = Column(String(32), comment = '测试责任人或者用例编写人员')
    tester          = Column(String(32), comment = '测试执行人或者运行该用例的人员')
    func            = Column(String(64), nullable = False, comment = 'api或者suite的函数名称(必填)， case无要求')
    case_type       = Column(SmallInteger, default = 0, comment = '0-api, 1-case, 2-suite')
       
    create_time     = Column(DateTime, nullable = False)
    update_time     = Column(DateTime, nullable = False)

    def __init__(self, project_id,desc,name,responsible,tester,func, case_type,create_time,update_time):  
        self.project_id  = project_id 
        self.desc        = desc       
        self.name        = name       
        self.responsible = responsible
        self.tester      = tester     
        self.func        = func       
        self.type        = case_type
        self.create_time = create_time
        self.update_time = update_time    
    
    def __repr__(self):
        return '<Case %r-%r>' % (self.name,self.id)

class CaseItemRequest(db.Model):
    ''' case item of request '''

    __tablename__ = 'case_item_request'
        
    id              = Column(Integer, primary_key=True)
    case_id         = Column(Integer, nullable = False, comment = '隶属于case表-关联case表')
    glob_var        = Column(String(512), comment = '全局变量（dict）')
    glob_regx       = Column(String(512), comment = '全局正则表达式（dict）')
    pre_command     = Column(String(512), comment = '测试用例前置条件(list)')
    url             = Column(String(512), nullable = False, comment = '请求url')
    method          = Column(String(4), nullable = False, comment = '请求方法(get or post)')
    hearders        = Column(String(1024), comment = '请求头(dict)')
    data            = Column(String(1024), comment = '请求体(dict or str)')
    post_command    = Column(String(512), comment = '测试用例后置条件(list)')
    verify          = Column(String(512), comment = '验证条件(list)')
        
    create_time     = Column(DateTime, nullable = False)
    update_time     = Column(DateTime, nullable = False)

    def __init__(self, case_id, glob_var, glob_regx,pre_command,url,method,hearders,data,post_command,verify,create_time,update_time):  
        self.case_id        = case_id 
        self.glob_var       = glob_var       
        self.glob_regx      = glob_regx
        self.pre_command    = pre_command
        self.url            = url
        self.method         = method
        self.hearders       = hearders
        self.data           = data
        self.post_command   = post_command
        self.verify         = verify
        self.create_time    = create_time
        self.update_time    = update_time
          
    
    def __repr__(self):
        return '<CaseItemRequest %r-%r>' % (self.url,self.id)
        



# # 执行
# class Run(db.Model):
#     ''' 执行集   -> 场景用例的运行集合 '''
#     __tablename__ = 'run'
#     
#     id          = Column(Integer, primary_key=True)
#     exec_date   = Column(Date)
#     exec_time   = Column(Time)
#     duration    = Column(Integer)
#     total_cases = Column(Integer)
#     pass_cases  = Column(Integer)
#     fail_cases  = Column(Integer)
#     
#     testsets        = relationship("TestSet", backref = "trun", lazy = "dynamic")
#     
#     def __init__(self, exec_date, exec_time, duration, total_cases, pass_cases, fail_cases):        
#         self.exec_date      = exec_date
#         self.exec_time      = exec_time
#         self.duration       = duration
#         self.total_cases    = total_cases
#         self.pass_cases     = pass_cases
#         self.fail_cases     = fail_cases
#     
#     def has_testsets(self, testset_obj):
#         return self.testsets.filter(TestSet.proj_name == testset_obj.proj_name).count() > 0
#     
#     def append_testsets(self, testset_obj):
#         if not self.has_testsets(testset_obj):
#             self.testsets.append(testset_obj)
#             return self
#     
#     def remove_testsets(self, testset_obj):
#         if self.has_testsets(testset_obj):
#             self.testsets.remove(testset_obj)
#     
#     def get_testsets(self):
#         return TestSet.query.join(Run).filter(TestSet.run_id == self.id).all()
#             
#     def __repr__(self):
#         return '<Run %r>' % (self.id)