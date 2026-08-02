#!/usr/bin/env python3
"""Application tracker CLI — log and query internship applications.

Usage:
  python3 tracker.py add --company Mercari --role "SWE Intern" --region Japan --status applied
  python3 tracker.py list                      # all applications
  python3 tracker.py list --status applied     # filter by status
  python3 tracker.py list --region Japan       # filter by region
  python3 tracker.py due                       # applications with next_action_date within 7 days
  python3 tracker.py summary                   # counts by status and region
"""

import argparse
import csv
import os
import sys
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "applications.csv")
FIELDS = [
    "company", "role", "region", "resume_variant", "repos_shown",
    "date_applied", "status", "deadline", "next_action", "next_action_date", "notes",
]


def load():
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def add(args):
    rows = load()
    row = {
        "company": args.company, "role": args.role or "", "region": args.region or "",
        "resume_variant": args.resume or "", "repos_shown": args.repos or "",
        "date_applied": args.date_applied or date.today().isoformat(),
        "status": args.status or "to_apply", "deadline": args.deadline or "",
        "next_action": args.next_action or "", "next_action_date": args.next_action_date or "",
        "notes": args.notes or "",
    }
    rows.append(row)
    save(rows)
    print(f"Added: {row['company']} / {row['role']} [{row['status']}]")


def _match(row, status, region, company):
    if status and row["status"] != status:
        return False
    if region and region.lower() not in row["region"].lower():
        return False
    if company and company.lower() not in row["company"].lower():
        return False
    return True


def list_(args):
    rows = [r for r in load() if _match(r, args.status, args.region, args.company)]
    if not rows:
        print("No applications match.")
        return
    print(f"{'company':<14}{'role':<22}{'region':<10}{'status':<10}{'applied':<12}{'next_action':<22}{'next_date'}")
    for r in rows:
        print(f"{r['company']:<14}{r['role'][:21]:<22}{r['region']:<10}{r['status']:<10}{r['date_applied']:<12}{r['next_action'][:21]:<22}{r['next_action_date']}")


def due(args):
    today = date.today()
    cutoff = today + timedelta(days=7)
    found = False
    for r in load():
        try:
            d = datetime.fromisoformat(r["next_action_date"]).date()
        except (ValueError, TypeError):
            continue
        if today <= d <= cutoff:
            found = True
            print(f"  {r['next_action']:<28} for {r['company']:<12} by {r['next_action_date']}")
    if not found:
        print("Nothing due in the next 7 days.")


def summary(args):
    rows = load()
    from collections import Counter
    by_status = Counter(r["status"] for r in rows)
    by_region = Counter(r["region"] for r in rows)
    print("By status:", dict(by_status) or "(none)")
    print("By region:", dict(by_region) or "(none)")
    print(f"Total: {len(rows)}")


def main():
    p = argparse.ArgumentParser(description="Internship application tracker")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="log a new application")
    pa.add_argument("--company", required=True)
    pa.add_argument("--role", default="")
    pa.add_argument("--region", default="")
    pa.add_argument("--resume", default="", help="resume variant filename")
    pa.add_argument("--repos", default="", help="comma-separated repos shown")
    pa.add_argument("--date-applied", default="")
    pa.add_argument("--status", default="to_apply", choices=["to_apply", "applied", "oa", "interview", "offer", "rejected"])
    pa.add_argument("--deadline", default="")
    pa.add_argument("--next-action", default="")
    pa.add_argument("--next-action-date", default="")
    pa.add_argument("--notes", default="")
    pa.set_defaults(func=add)

    pl = sub.add_parser("list", help="list applications")
    pl.add_argument("--status", default="")
    pl.add_argument("--region", default="")
    pl.add_argument("--company", default="")
    pl.set_defaults(func=list_)

    pd = sub.add_parser("due", help="show actions due in the next 7 days")
    pd.set_defaults(func=due)

    ps = sub.add_parser("summary", help="counts by status and region")
    ps.set_defaults(func=summary)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
