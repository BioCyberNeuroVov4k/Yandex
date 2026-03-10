'''with WaitTimes as (
  Select
     strftime('%Y-%m-%d', l2.verdict_time) as field_date
    ,julianday(l2.verdict_time) - julianday(l1.verdict_time) as wait_time
  From logs as l1
  inner join logs as l2
    ON l1.campaign_id = l2.campaign_id
  Where 1 = 1
        and l1.verdict = 'No' and l2.verdict = 'Yes'
        and l1.verdict_time < l2.verdict_time
        and not exists (
      Select
        1
      From logs as l3
      Where 1 = 1
            and l3.campaign_id = l1.campaign_id
            and l3.verdict = 'No'
            and l1.verdict_time < l3.verdict_time
            and l3.verdict_time < l2.verdict_time
    )
  Group by
    l2.verdict_time
)
Select
   field_date
  ,round(avg(wait_time) * 24 * 60) as avg_wait_time
From WaitTimes
Group by 1
Order by 1;'''