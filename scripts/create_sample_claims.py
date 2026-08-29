from pathlib import Path

DATA = {
    "data/policies/homeowners_basic.txt": "Homeowners Policy HO-3\n\nCoverage A covers direct physical loss to the dwelling caused by a covered peril, subject to deductible and exclusions. Water damage caused by sudden and accidental discharge from plumbing is covered. Flood damage is excluded.",
    "data/endorsements/water_backup.txt": "Water Backup Endorsement\n\nThis endorsement provides up to $10,000 for direct physical loss caused by water which backs up through sewers or drains, subject to the endorsement deductible.",
    "data/procedures/water_claims.txt": "Water Claim Procedure\n\nDocument the source of water, confirm whether the discharge was sudden and accidental, and determine whether a flood exclusion or water-backup endorsement applies.",
}

if __name__ == "__main__":
    for filename, content in DATA.items():
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print("Sample policy documents created.")
