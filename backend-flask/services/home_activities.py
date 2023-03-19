from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import pool

# tracer = trace.get_tracer("home.activities")
class HomeActivities:
    def run(cognito_user_id=None):
        print("HOME ACTIVITY")
        #logger.info("homeActivities")
        # with tracer.start_as_current_span("home.activities.mock.data"):
        # now = datetime.now(timezone.utc).astimezone()
        sql = """
            SELECT * from activities   
        """

        with pool.connection() as conn:
          with conn.cursor() as cur:
              cur.execute(sql)
              # this will return a tuple
              # the first field being the data
              json = cur.fetchone()

        print("=3---------")
        print("==---------")   
        for record in cur:
          print(record)
        print(json)           
        return json[0]
