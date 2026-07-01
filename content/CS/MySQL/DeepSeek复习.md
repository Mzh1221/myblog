## 一、连接与退出 MySQL

```sql
-- 连接本地 MySQL（默认端口3306）
mysql -u 用户名 -p

-- 连接远程主机
mysql -h 主机IP -u 用户名 -p

-- 退出
exit;
-- 或
quit;
```

---

## 二、数据库操作（DDL 的一部分）

```sql
-- 查看所有数据库
SHOW DATABASES;

-- 创建数据库
CREATE DATABASE 数据库名;
-- 指定字符集（推荐）
CREATE DATABASE 数据库名 DEFAULT CHARSET=utf8mb4;

-- 选择/切换数据库
USE 数据库名;

-- 查看当前所在数据库
SELECT DATABASE();

-- 删除数据库（慎用）
DROP DATABASE 数据库名;
```

---

## 三、表操作（DDL）

### 1. 创建表
```sql
CREATE TABLE 表名 (
    字段名1 数据类型 [约束],
    字段名2 数据类型 [约束],
    ...
    PRIMARY KEY (字段名)
);
```
示例：
```sql
CREATE TABLE student (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    age INT,
    sex CHAR(1) DEFAULT '男'
);
```

### 2. 查看表
```sql
-- 查看当前数据库所有表
SHOW TABLES;

-- 查看表结构
DESC 表名;
-- 或
DESCRIBE 表名;

-- 查看建表语句
SHOW CREATE TABLE 表名;
```

### 3. 修改表（ALTER）
```sql
-- 添加字段
ALTER TABLE 表名 ADD 字段名 数据类型 [约束];

-- 修改字段类型
ALTER TABLE 表名 MODIFY 字段名 新数据类型;

-- 修改字段名+类型
ALTER TABLE 表名 CHANGE 旧字段名 新字段名 新数据类型;

-- 删除字段
ALTER TABLE 表名 DROP 字段名;

-- 重命名表
RENAME TABLE 旧表名 TO 新表名;
```

### 4. 删除表
```sql
DROP TABLE 表名;
```

---

## 四、数据操作（DML）

### 1. 插入数据（INSERT）
```sql
-- 插入全部字段
INSERT INTO 表名 VALUES (值1, 值2, ...);

-- 插入指定字段
INSERT INTO 表名 (字段1, 字段2) VALUES (值1, 值2);

-- 批量插入
INSERT INTO 表名 (字段1, 字段2) VALUES 
    (值1, 值2),
    (值3, 值4);
```

### 2. 更新数据（UPDATE）
```sql
UPDATE 表名 SET 字段1=新值1, 字段2=新值2 WHERE 条件;
-- 注意：不加 WHERE 会更新全表！
```

### 3. 删除数据（DELETE）
```sql
DELETE FROM 表名 WHERE 条件;
-- 不加 WHERE 会删除全表数据（但表结构保留）

-- 清空全表（效率更高，重置自增）
TRUNCATE TABLE 表名;
```

---

## 五、查询操作（DQL）—— 重点

### 1. 基础查询
```sql
-- 查询所有字段
SELECT * FROM 表名;

-- 查询指定字段
SELECT 字段1, 字段2 FROM 表名;

-- 去重
SELECT DISTINCT 字段 FROM 表名;

-- 起别名（AS 可省略）
SELECT 字段 AS 别名 FROM 表名;
```

### 2. 条件查询（WHERE）
```sql
SELECT * FROM 表名 WHERE 条件;
-- 条件运算符：=, !=/>, <, >=, <=
-- 逻辑：AND, OR, NOT
-- 范围：BETWEEN ... AND ...
-- 集合：IN (值1, 值2, ...)
-- 模糊：LIKE（% 任意多个，_ 单个）
-- 空值：IS NULL, IS NOT NULL
```

示例：
```sql
SELECT * FROM student WHERE age BETWEEN 18 AND 22;
SELECT * FROM student WHERE name LIKE '张%';
SELECT * FROM student WHERE sex IS NOT NULL;
```

### 3. 排序（ORDER BY）
```sql
SELECT * FROM 表名 ORDER BY 字段1 [ASC|DESC], 字段2 [ASC|DESC];
-- ASC 升序（默认），DESC 降序
```

### 4. 聚合函数
```sql
COUNT(*)     -- 计数
SUM(字段)    -- 求和
AVG(字段)    -- 平均值
MAX(字段)    -- 最大值
MIN(字段)    -- 最小值
```

### 5. 分组（GROUP BY）+ 过滤（HAVING）
```sql
SELECT 分组字段, 聚合函数
FROM 表名
WHERE 条件
GROUP BY 分组字段
HAVING 聚合函数条件;
-- WHERE 在分组前过滤，HAVING 在分组后过滤
```

示例：
```sql
SELECT sex, COUNT(*) AS 人数
FROM student
GROUP BY sex
HAVING COUNT(*) > 5;
```

### 6. 分页（LIMIT）
```sql
-- 前 10 条
SELECT * FROM 表名 LIMIT 10;

-- 跳过 5 条，取 10 条（第6~15条）
SELECT * FROM 表名 LIMIT 5, 10;
-- 或
SELECT * FROM 表名 LIMIT 10 OFFSET 5;
```

---

## 六、约束（完整性约束）

| 约束 | 关键字 | 说明 |
|------|--------|------|
| 主键 | `PRIMARY KEY` | 唯一且非空，一张表只能一个 |
| 唯一 | `UNIQUE` | 值不可重复，允许一个 NULL |
| 非空 | `NOT NULL` | 必须有值 |
| 默认 | `DEFAULT` | 未指定时使用默认值 |
| 外键 | `FOREIGN KEY` | 关联其他表的主键 |

---

## 七、用户与权限（DCL）

```sql
-- 创建用户
CREATE USER '用户名'@'主机' IDENTIFIED BY '密码';

-- 授权
GRANT 权限 ON 数据库.表 TO '用户名'@'主机';
-- 例如：GRANT SELECT, INSERT ON test.* TO 'tom'@'localhost';

-- 撤销权限
REVOKE 权限 ON 数据库.表 FROM '用户名'@'主机';

-- 查看权限
SHOW GRANTS FOR '用户名'@'主机';

-- 删除用户
DROP USER '用户名'@'主机';

-- 刷新权限（修改后生效）
FLUSH PRIVILEGES;
```

---

## 八、常用辅助命令

```sql
-- 查看当前 MySQL 版本
SELECT VERSION();

-- 查看当前用户
SELECT USER();

-- 查看所有正在运行的进程
SHOW PROCESSLIST;

-- 查看存储引擎
SHOW ENGINES;

-- 查看字符集设置
SHOW VARIABLES LIKE 'character%';
```

---

## ✅ 快速记忆口诀（帮你梳理）

- **DDL**（定义）：CREATE / ALTER / DROP  
- **DML**（操作）：INSERT / UPDATE / DELETE  
- **DQL**（查询）：SELECT  
- **DCL**（控制）：GRANT / REVOKE  
- **TCL**（事务）：COMMIT / ROLLBACK / SAVEPOINT

---

## 一、多表连接（JOIN）

### 1. 连接类型总览

| 连接类型 | 关键字                | 说明                        |
| ---- | ------------------ | ------------------------- |
| 内连接  | `INNER JOIN(JOIN)` | 只返回两表匹配的行                 |
| 左外连接 | `LEFT JOIN`        | 返回左表全部 + 右表匹配的行，不匹配则 NULL |
| 右外连接 | `RIGHT JOIN`       | 返回右表全部 + 左表匹配的行，不匹配则 NULL |
| 全外连接 | `FULL JOIN`        | MySQL 不直接支持（可用 UNION 模拟）  |
| 交叉连接 | `CROSS JOIN`       | 笛卡尔积（慎用）                  |
| 自连接  | 表自身连接              | 同一张表当作两张表用                |

---

### 2. 内连接（INNER JOIN）
**只返回两表都匹配的记录**

```sql
-- 标准写法
SELECT s.name, c.course_name
FROM student s
INNER JOIN score sc ON s.id = sc.student_id
INNER JOIN course c ON sc.course_id = c.id;

-- 等价写法（老式）
SELECT s.name, c.course_name
FROM student s, score sc, course c
WHERE s.id = sc.student_id AND sc.course_id = c.id;
```

---

### 3. 左外连接（LEFT JOIN）
**左表全部显示，右表只显示匹配的，不匹配则补 NULL**

```sql
-- 查询所有学生及其成绩（没选课的学生也显示）
SELECT s.name, sc.score
FROM student s
LEFT JOIN score sc ON s.id = sc.student_id;
```

---

### 4. 右外连接（RIGHT JOIN）
**右表全部显示，左表只显示匹配的**

```sql
-- 查询所有课程及其选课学生（没被选的课程也显示）
SELECT c.course_name, s.name
FROM student s
RIGHT JOIN score sc ON s.id = sc.student_id
RIGHT JOIN course c ON sc.course_id = c.id;
```

---

### 5. 自连接（Self JOIN）
**一张表当作两张表用，必须起别名**

```sql
-- 查询每个员工的上级领导（员工表包含 manager_id）
SELECT e.name AS 员工, m.name AS 领导
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.id;
```

---

### 6. 全外连接模拟（UNION）
```sql
-- MySQL 用 LEFT JOIN + RIGHT JOIN + UNION 模拟 FULL OUTER JOIN
SELECT * FROM student s LEFT JOIN score sc ON s.id = sc.student_id
UNION
SELECT * FROM student s RIGHT JOIN score sc ON s.id = sc.student_id;
```

---

## 二、子查询

### 1. 子查询位置
| 位置 | 说明 |
|------|------|
| `WHERE` 中 | 最常用，作为条件 |
| `SELECT` 中 | 作为字段值 |
| `FROM` 中 | 作为派生表（必须起别名） |
| `HAVING` 中 | 作为分组后的条件 |

---

### 2. 单行子查询（返回一个值）
```sql
-- 查询年龄大于平均年龄的学生
SELECT * FROM student 
WHERE age > (SELECT AVG(age) FROM student);
```

---

### 3. 多行子查询（返回一列多行）
配合 `IN`、`ANY`、`ALL` 使用：

```sql
-- 查询选修了课程的学生（IN）
SELECT * FROM student 
WHERE id IN (SELECT DISTINCT student_id FROM score);

-- 查询比任一（ANY）计算机系学生年龄大的学生
SELECT * FROM student 
WHERE age > ANY (SELECT age FROM student WHERE dept='计算机');

-- 查询比所有（ALL）计算机系学生年龄大的学生
SELECT * FROM student 
WHERE age > ALL (SELECT age FROM student WHERE dept='计算机');
```

---

### 4. EXISTS 子查询（相关子查询）
```sql
-- 查询选修了课程的学生（用 EXISTS 实现）
SELECT * FROM student s
WHERE EXISTS (SELECT 1 FROM score sc WHERE sc.student_id = s.id);
```
> `EXISTS` 效率高，因为只要找到一条就停止，适合大数据量。

---

### 5. FROM 中的派生表
```sql
-- 查询每个学生各科成绩的平均分
SELECT s.name, t.avg_score
FROM student s
JOIN (SELECT student_id, AVG(score) AS avg_score FROM score GROUP BY student_id) t
ON s.id = t.student_id;
```

---

## 三、事务命令（TCL）

### 1. 事务四大特性（ACID）
| 特性 | 说明 |
|------|------|
| **原子性** | 要么全成功，要么全回滚 |
| **一致性** | 事务前后数据状态一致 |
| **隔离性** | 并发事务互不干扰（隔离级别控制） |
| **持久性** | 提交后数据永久保存 |

---

### 2. 事务相关命令
```sql
-- 查看当前自动提交状态（默认为 ON）
SHOW VARIABLES LIKE 'autocommit';

-- 关闭自动提交（改为手动）
SET autocommit = 0;

-- 开启事务（方式1）
START TRANSACTION;

-- 开启事务（方式2）
BEGIN;

-- 提交事务
COMMIT;

-- 回滚事务（撤销未提交的操作）
ROLLBACK;

-- 设置保存点
SAVEPOINT sp1;

-- 回滚到保存点
ROLLBACK TO SAVEPOINT sp1;

-- 删除保存点
RELEASE SAVEPOINT sp1;
```

---

### 3. 事务隔离级别
| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
|----------|------|------------|------|
| `READ UNCOMMITTED` | ✅ 可能 | ✅ 可能 | ✅ 可能 |
| `READ COMMITTED` | ❌ | ✅ 可能 | ✅ 可能 |
| `REPEATABLE READ`（默认） | ❌ | ❌ | ✅ 可能 |
| `SERIALIZABLE` | ❌ | ❌ | ❌ |

```sql
-- 查看当前隔离级别
SELECT @@transaction_isolation;

-- 设置隔离级别
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

---

## 四、索引（Index）

### 1. 索引类型
| 类型 | 关键字 | 说明 |
|------|--------|------|
| 普通索引 | `INDEX` | 无约束，仅加速查询 |
| 唯一索引 | `UNIQUE INDEX` | 值不能重复，允许一个 NULL |
| 主键索引 | `PRIMARY KEY` | 唯一且非空，一张表一个 |
| 全文索引 | `FULLTEXT` | 用于大文本搜索（MyISAM/InnoDB 5.6+） |
| 组合索引 | 多字段联合 | 最左前缀匹配原则 |

---

### 2. 创建与删除索引
```sql
-- 建表时创建
CREATE TABLE t (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    INDEX idx_name (name)
);

-- 已存在表添加索引
CREATE INDEX idx_name ON 表名 (字段);
CREATE UNIQUE INDEX idx_unique ON 表名 (字段);
ALTER TABLE 表名 ADD INDEX idx_name (字段);

-- 删除索引
DROP INDEX idx_name ON 表名;
ALTER TABLE 表名 DROP INDEX idx_name;
```

---

### 3. 查看索引
```sql
-- 查看表的索引
SHOW INDEX FROM 表名;

-- 查看执行计划（判断索引是否被使用）
EXPLAIN SELECT * FROM 表名 WHERE 字段 = '值';
```

---

### 4. 索引使用原则（重要！）
| 原则 | 说明 |
|------|------|
| **最左前缀** | 组合索引 `(a,b,c)` 能用到 `a`、`a,b`、`a,b,c`，不能跳过 |
| **模糊查询** | `LIKE '张%'` 可用索引，`LIKE '%张'` 不用索引 |
| **列独立** | `WHERE age+1=20` 不用索引，改为 `WHERE age=19` |
| **区分度高** | 重复率高的字段（如性别）建索引效果差 |
| **避免过多索引** | 索引占用空间，影响 INSERT/UPDATE 性能 |

---

### 5. 索引的优缺点
| 优点 | 缺点 |
|------|------|
| 大幅提升查询速度 | 占用额外存储空间 |
| 唯一索引保证数据唯一性 | 增删改需要维护索引，降低写入速度 |
| 加速 ORDER BY / GROUP BY | 索引过多可能导致优化器选择错误 |

---

### ## 关系的完整性约束

| 约束类型        | 说明                    | 示例                                    |
| ----------- | --------------------- | ------------------------------------- |
| **实体完整性**   | 主键不能为空且唯一             | `PRIMARY KEY`                         |
| **参照完整性**   | 外键值必须存在于被参照表中，或为 NULL | `FOREIGN KEY`                         |
| **用户定义完整性** | 业务规则约束                | `NOT NULL`、`UNIQUE`、`CHECK`、`DEFAULT` |

