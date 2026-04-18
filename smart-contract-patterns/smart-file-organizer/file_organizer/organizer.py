"""Smart file organizer with AI suggestions."""

import shutil
from pathlib import Path
from typing import Dict, List
from datetime import datetime

class SmartOrganizer:
    """Organize files based on AI classification."""
    
    def __init__(self, source_dir: str, dest_dir: str):
        self.source = Path(source_dir)
        self.dest = Path(dest_dir)
        self.dest.mkdir(parents=True, exist_ok=True)
    
    def organize_by_type(self, dry_run: bool = False) -> Dict:
        """Organize files by type."""
        from .classifier import FileClassifier
        
        classifier = FileClassifier()
        stats = {'moved': 0, 'errors': 0, 'by_category': {}}
        
        for file in self.source.rglob('*'):
            if file.is_file():
                info = classifier.classify(str(file))
                category = info['category']
                
                # Create category folder
                cat_folder = self.dest / category
                cat_folder.mkdir(exist_ok=True)
                
                # Move file
                dest_file = cat_folder / file.name
                if not dry_run:
                    try:
                        shutil.move(str(file), str(dest_file))
                        stats['moved'] += 1
                        stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
                    except Exception as e:
                        stats['errors'] += 1
                else:
                    stats['moved'] += 1
        
        return stats
    
    def organize_by_date(self, dry_run: bool = False) -> Dict:
        """Organize files by creation date."""
        stats = {'moved': 0, 'errors': 0}
        
        for file in self.source.rglob('*'):
            if file.is_file():
                mtime = datetime.fromtimestamp(file.stat().st_mtime)
                date_folder = self.dest / str(mtime.year) / f"{mtime.month:02d}"
                date_folder.mkdir(parents=True, exist_ok=True)
                
                dest_file = date_folder / file.name
                if not dry_run:
                    try:
                        shutil.move(str(file), str(dest_file))
                        stats['moved'] += 1
                    except:
                        stats['errors'] += 1
                else:
                    stats['moved'] += 1
        
        return stats
