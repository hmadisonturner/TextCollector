# Contributing to TextCollector

This document outlines the development workflow for TextCollector, with special focus on the documentation-driven approach.

## Development Workflow

TextCollector follows a documentation-driven development approach:

1. **Documentation First**
   - Start with specification documents in `/docs/specifications`
   - Document architectural decisions in `/docs/architecture/adr`
   - Outline implementation plans in `/docs/planning`

2. **Issue Creation**
   - Create GitHub issues based on specifications
   - Link issues to relevant documentation
   - Break down large features into manageable tasks

3. **Branch Strategy**
   - Feature branches: `feature/descriptive-name`
   - Bug fixes: `fix/issue-description`
   - Documentation: `docs/topic-name`
   - Follow the branch naming convention consistently

4. **Code Development**
   - Follow Google Python Style Guide
   - Include docstrings for all functions
   - Add appropriate type hints
   - Keep functions focused and modular

5. **Testing Requirements**
   - Write tests before or alongside code
   - Ensure test coverage for new functionality
   - Include both unit and integration tests
   - Tests should be in the corresponding `tests/` directory

6. **Review Process**
   - Self-review code before submission
   - Create detailed pull requests referencing issues
   - Ensure all tests pass
   - Address all feedback from reviewers

7. **Documentation Updates**
   - Update relevant documentation with code changes
   - Include API documentation for new features
   - Ensure user guides reflect new functionality
   - Document any breaking changes clearly

## Converting Planning to Implementation

To convert planning documents into actionable development:

1. **From Specifications to Issues**
   - Review specification documents
   - Create GitHub issues for each major component
   - Link to the relevant specification section
   - Add appropriate labels (feature, enhancement, etc.)

2. **From ADRs to Architecture**
   - Reference ADRs when implementing architectural components
   - Ensure implementation follows the documented decisions
   - Update ADRs if architectural changes are necessary

3. **From Roadmap to Milestones**
   - Use roadmap phases to create GitHub milestones
   - Assign issues to appropriate milestones
   - Track progress against roadmap timelines

4. **From Tasks to Pull Requests**
   - Create branches for individual issues
   - Reference issue numbers in commits
   - Create pull requests that close specific issues
   - Include implementation details and testing notes

## Documentation Standards

When contributing to documentation:

1. **Use Markdown consistently**
   - Follow standard Markdown formatting
   - Use headers, lists, and code blocks appropriately
   - Include diagrams when helpful (using Mermaid or images)

2. **Documentation Structure**
   - Place documents in the appropriate directory
   - Follow established document templates
   - Link related documents for context

3. **Content Guidelines**
   - Be clear and concise
   - Include examples where applicable
   - Avoid jargon unless necessary
   - Define technical terms on first use

4. **Versioning Awareness**
   - Indicate which software version the documentation applies to
   - Update documentation when API or behavior changes
   - Maintain backward compatibility notes when appropriate

## Getting Started

1. Fork the repository
2. Review the documentation to understand the project
3. Set up your development environment
4. Choose an issue to work on
5. Create a branch for your changes
6. Make your changes following the guidelines above
7. Submit a pull request with a clear description of changes