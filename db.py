
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnection():
    # 初始化数据库连接:
    engine = create_engine('postgresql://postgres:127.0.0.1@localhost:5432/postgres')

    def get_db_connection(self):
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=self.engine)
        return DBSession()
