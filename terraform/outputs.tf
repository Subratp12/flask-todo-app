output "ecr_repository_name" {
  description = "The name of the ECR repository"
  value       = aws_ecr_repository.foo.name
}

output "ecr_repository_url" {
  description = "The URL of the ECR repository"
  value       = aws_ecr_repository.foo.repository_url
}
