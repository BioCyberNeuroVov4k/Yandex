with companies as (
    select
        b.name,
        a.date,
        max(a.rk_id) as max_rk_id
    from 
        payment_date a
        join users b on b.id = a.user_id
        join advertising_companies c on c.id = a.rk_id
    where 1=1
        and owner_id is not null -- признак компании
        and c.is_main = 1
        and a.sum > 0
    group by
        b.name,
        a.date
)

select
    bb.name,
    sum(aa.sum) as budget
from advertising_companies aa
join companies bb on bb.max_rk_id = aa.rk_id
group by bb.name
order by 1 asc;



with WaitTimes as (
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
Order by 1;