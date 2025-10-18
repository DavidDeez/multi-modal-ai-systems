import time
import statistics
from typing import List, Dict, Any

class BenchmarkSuite:
    def __init__(self):
        self.results = []
    
    def benchmark_architecture(self, architecture, test_cases: List[Dict]) -> Dict[str, Any]:
        """Benchmark an architecture with multiple test cases"""
        latencies = []
        successes = 0
        
        for test_case in test_cases:
            start_time = time.time()
            
            try:
                if test_case['type'] == 'text':
                    result = architecture.process_text_direct(test_case['input'])
                elif test_case['type'] == 'audio':
                    result = architecture.process_audio_chat(test_case['input'])
                elif test_case['type'] == 'vision':
                    result = architecture.process_vision_direct(test_case['input'])
                
                latency = time.time() - start_time
                latencies.append(latency)
                
                if 'error' not in result:
                    successes += 1
                    
            except Exception as e:
                latencies.append(10.0)  # Penalty for failure
        
        return {
            "architecture": architecture.__class__.__name__,
            "total_tests": len(test_cases),
            "success_rate": successes / len(test_cases),
            "avg_latency": statistics.mean(latencies) if latencies else 0,
            "max_latency": max(latencies) if latencies else 0,
            "min_latency": min(latencies) if latencies else 0
        }
    
    def compare_architectures(self, architectures: List, test_cases: List[Dict]) -> List[Dict]:
        """Compare multiple architectures"""
        comparison = []
        for arch in architectures:
            result = self.benchmark_architecture(arch, test_cases)
            comparison.append(result)
        
        self.results = comparison
        return comparison
