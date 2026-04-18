"""AI-powered file classification."""

import mimetypes
from pathlib import Path
from typing import Dict, List
import hashlib

class FileClassifier:
    """Classify files by content and metadata."""
    
    CATEGORIES = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
        'data': ['.json', '.xml', '.csv', '.xlsx', '.db', '.sql'],
        'media': ['.mp3', '.mp4', '.avi', '.mov', '.wav', '.flac'],
        'archives': ['.zip', '.tar', '.gz', '.bz2', '.7z', '.rar'],
    }
    
    def classify(self, file_path: str) -> Dict:
        """Classify a single file."""
        path = Path(file_path)
        ext = path.suffix.lower()
        
        # Determine category
        category = 'other'
        for cat, extensions in self.CATEGORIES.items():
            if ext in extensions:
                category = cat
                break
        
        # Calculate file hash
        file_hash = hashlib.md5(path.read_bytes()).hexdigest()[:8] if path.exists() else None
        
        return {
            'path': str(path),
            'name': path.name,
            'extension': ext,
            'category': category,
            'size': path.stat().st_size if path.exists() else 0,
            'hash': file_hash
        }
    
    def find_duplicates(self, directory: str) -> List[List[str]]:
        """Find duplicate files by hash."""
        hashes = {}
        for file in Path(directory).rglob('*'):
            if file.is_file():
                file_hash = hashlib.md5(file.read_bytes()).hexdigest()
                if file_hash in hashes:
                    hashes[file_hash].append(str(file))
                else:
                    hashes[file_hash] = [str(file)]
        
        return [files for files in hashes.values() if len(files) > 1]
