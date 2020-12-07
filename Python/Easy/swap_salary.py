"""
    SQL QUERY: 
    Given a table salary, such as the one below, that has m=male and f=female values. 
    Swap all f and m values (i.e., change all f values to m and vice versa) with a single update statement and no intermediate temp table.
"""

"""Answer:
        UPDATE salary SET sex = IF(sex = 'm', 'f', 'm')
"""